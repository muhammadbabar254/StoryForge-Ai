"""StoryForge AI — main story generation pipeline."""

import datetime
import json
import os
import time

import Writer.Chapter.ChapterDetector
import Writer.Chapter.ChapterGenerator
import Writer.Config
import Writer.Interface.Wrapper
import Writer.NovelEditor
import Writer.OutlineGenerator
import Writer.PrintUtils
import Writer.Scrubber
import Writer.Statistics
import Writer.StoryInfo
import Writer.Translator

from storyforge.branding import APP_NAME, GENERATOR_ID, print_banner
from storyforge.builders.character import build_characters, format_for_prompt as format_characters
from storyforge.builders.timeline import build_timeline, format_timeline_markdown
from storyforge.builders.world import build_world, format_for_prompt as format_world
from storyforge.export.epub import export_epub
from storyforge.export.pdf import export_pdf
from storyforge.history.store import record_story


class GenerationOptions:
    """Runtime options for a story generation run."""

    def __init__(self, args):
        self.prompt_path = args.Prompt
        self.output = args.Output
        self.seed = args.Seed
        self.translate = args.Translate
        self.translate_prompt = args.TranslatePrompt
        self.character_builder = getattr(args, "CharacterBuilder", False)
        self.world_builder = getattr(args, "WorldBuilder", False)
        self.build_timeline = getattr(args, "BuildTimeline", True)
        self.export_pdf = getattr(args, "ExportPDF", False)
        self.export_epub = getattr(args, "ExportEPUB", False)
        self.show_banner = getattr(args, "ShowBanner", True)


def apply_config(args):
    """Apply CLI arguments to Writer.Config."""
    Writer.Config.SEED = args.Seed
    Writer.Config.INITIAL_OUTLINE_WRITER_MODEL = args.InitialOutlineModel
    Writer.Config.CHAPTER_OUTLINE_WRITER_MODEL = args.ChapterOutlineModel
    Writer.Config.CHAPTER_STAGE1_WRITER_MODEL = args.ChapterS1Model
    Writer.Config.CHAPTER_STAGE2_WRITER_MODEL = args.ChapterS2Model
    Writer.Config.CHAPTER_STAGE3_WRITER_MODEL = args.ChapterS3Model
    Writer.Config.CHAPTER_STAGE4_WRITER_MODEL = args.ChapterS4Model
    Writer.Config.CHAPTER_REVISION_WRITER_MODEL = args.ChapterRevisionModel
    Writer.Config.EVAL_MODEL = args.EvalModel
    Writer.Config.REVISION_MODEL = args.RevisionModel
    Writer.Config.INFO_MODEL = args.InfoModel
    Writer.Config.SCRUB_MODEL = args.ScrubModel
    Writer.Config.CHECKER_MODEL = args.CheckerModel
    Writer.Config.TRANSLATOR_MODEL = args.TranslatorModel
    Writer.Config.TRANSLATE_LANGUAGE = args.Translate
    Writer.Config.TRANSLATE_PROMPT_LANGUAGE = args.TranslatePrompt
    Writer.Config.OUTLINE_MIN_REVISIONS = args.OutlineMinRevisions
    Writer.Config.OUTLINE_MAX_REVISIONS = args.OutlineMaxRevisions
    Writer.Config.CHAPTER_MIN_REVISIONS = args.ChapterMinRevisions
    Writer.Config.CHAPTER_MAX_REVISIONS = args.ChapterMaxRevisions
    Writer.Config.CHAPTER_NO_REVISIONS = args.NoChapterRevision
    Writer.Config.SCRUB_NO_SCRUB = args.NoScrubChapters
    Writer.Config.EXPAND_OUTLINE = args.ExpandOutline
    Writer.Config.ENABLE_FINAL_EDIT_PASS = args.EnableFinalEditPass
    Writer.Config.OPTIONAL_OUTPUT_NAME = args.Output
    Writer.Config.SCENE_GENERATION_PIPELINE = args.SceneGenerationPipeline
    Writer.Config.DEBUG = args.Debug


def get_models(args) -> list:
    return list(
        {
            args.InitialOutlineModel,
            args.ChapterOutlineModel,
            args.ChapterS1Model,
            args.ChapterS2Model,
            args.ChapterS3Model,
            args.ChapterS4Model,
            args.ChapterRevisionModel,
            args.EvalModel,
            args.RevisionModel,
            args.InfoModel,
            args.ScrubModel,
            args.CheckerModel,
            args.TranslatorModel,
        }
    )


def run_pipeline(args) -> dict:
    """Execute the full StoryForge AI generation pipeline."""
    start_time = time.time()
    opts = GenerationOptions(args)

    if opts.show_banner:
        print_banner()

    apply_config(args)
    models = get_models(args)

    logger = Writer.PrintUtils.Logger()
    logger.Log(f"{APP_NAME} — Initializing LLM interface", 5)
    interface = Writer.Interface.Wrapper.Interface(models)

    if opts.prompt_path is None:
        raise ValueError("No prompt file provided. Use -Prompt <path>")

    with open(opts.prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()
    base_prompt = prompt

    if Writer.Config.TRANSLATE_PROMPT_LANGUAGE:
        prompt = Writer.Translator.TranslatePrompt(
            interface, logger, prompt, Writer.Config.TRANSLATE_PROMPT_LANGUAGE
        )

    # --- StoryForge Builders ---
    character_data = {}
    world_data = {}
    builder_context = ""

    if opts.character_builder:
        logger.Log("StoryForge Character Builder — generating profiles", 3)
        character_data = build_characters(interface, logger, prompt)
        builder_context += format_characters(character_data) + "\n\n"

    if opts.world_builder:
        logger.Log("StoryForge World Builder — generating world profile", 3)
        world_data = build_world(interface, logger, prompt)
        builder_context += format_world(world_data) + "\n\n"

    enriched_prompt = prompt
    if builder_context:
        enriched_prompt = f"{builder_context}\n\n# Story Prompt\n{prompt}"

    outline, elements, rough_outline, base_context = (
        Writer.OutlineGenerator.GenerateOutline(
            interface, logger, enriched_prompt, Writer.Config.OUTLINE_QUALITY
        )
    )

    logger.Log("Detecting chapters", 5)
    messages = [interface.BuildUserQuery(outline)]
    num_chapters = Writer.Chapter.ChapterDetector.LLMCountChapters(
        interface, logger, interface.GetLastMessageText(messages)
    )
    logger.Log(f"Found {num_chapters} chapter(s)", 5)

    chapter_outlines = []
    if Writer.Config.EXPAND_OUTLINE:
        expand_prompt = f"Please help me expand upon the following outline, chapter by chapter.\n\n```\n{outline}\n```\n"
        messages = [interface.BuildUserQuery(expand_prompt)]
        for chapter in range(1, num_chapters + 1):
            ch_outline, messages = Writer.OutlineGenerator.GeneratePerChapterOutline(
                interface, logger, chapter, outline, messages
            )
            chapter_outlines.append(ch_outline)

    detailed_outline = "".join(chapter_outlines)
    used_outline = outline
    if Writer.Config.EXPAND_OUTLINE:
        used_outline = f"\n# Base Outline\n{elements}\n\n# Detailed Outline\n{detailed_outline}\n"

    logger.Log("Starting chapter writing", 5)
    chapters = []
    for i in range(1, num_chapters + 1):
        chapter = Writer.Chapter.ChapterGenerator.GenerateChapter(
            interface,
            logger,
            i,
            num_chapters,
            used_outline,
            chapters,
            Writer.Config.OUTLINE_QUALITY,
            base_context,
        )
        chapter = f"### Chapter {i}\n\n{chapter}"
        chapters.append(chapter)
        logger.Log(
            f"Chapter {i} word count: {Writer.Statistics.GetWordCount(chapter)}", 2
        )

    story_info: dict = {
        "Outline": outline,
        "StoryElements": elements,
        "RoughChapterOutline": rough_outline,
        "BaseContext": base_context,
    }

    if opts.character_builder:
        story_info["Characters"] = character_data
    if opts.world_builder:
        story_info["World"] = world_data

    if Writer.Config.ENABLE_FINAL_EDIT_PASS:
        new_chapters = Writer.NovelEditor.EditNovel(
            interface, logger, chapters, outline, num_chapters
        )
    else:
        new_chapters = chapters
    story_info["UnscrubbedChapters"] = new_chapters

    if not Writer.Config.SCRUB_NO_SCRUB:
        new_chapters = Writer.Scrubber.ScrubNovel(
            interface, logger, new_chapters, num_chapters
        )
    else:
        logger.Log("Skipping scrubbing (disabled in config)", 4)
    story_info["ScrubbedChapters"] = new_chapters

    if Writer.Config.TRANSLATE_LANGUAGE:
        new_chapters = Writer.Translator.TranslateNovel(
            interface,
            logger,
            new_chapters,
            num_chapters,
            Writer.Config.TRANSLATE_LANGUAGE,
        )
    else:
        logger.Log("No translation requested", 4)
    story_info["TranslatedChapters"] = new_chapters

    story_body = "\n\n\n".join(new_chapters)

    messages = [interface.BuildUserQuery(outline)]
    info = Writer.StoryInfo.GetStoryInfo(interface, logger, messages)
    title = info["Title"]
    summary = info["Summary"]
    tags = info["Tags"]
    story_info.update({"Title": title, "Summary": summary, "Tags": tags})

    # --- Story Timeline ---
    timeline_data = {}
    if opts.build_timeline:
        logger.Log("StoryForge Timeline — building narrative timeline", 3)
        timeline_data = build_timeline(
            interface, logger, title, outline, new_chapters
        )
        story_info["Timeline"] = timeline_data

    print("─" * 60)
    print(f"  Title:   {title}")
    print(f"  Summary: {summary}")
    print(f"  Tags:    {tags}")
    print("─" * 60)

    elapsed = time.time() - start_time
    total_words = Writer.Statistics.GetWordCount(story_body)

    stats = _build_stats_string(
        title, summary, tags, total_words, elapsed, base_prompt
    )

    os.makedirs("Stories", exist_ok=True)
    fname = f"Stories/Story_{title.replace(' ', '_')}"
    if Writer.Config.OPTIONAL_OUTPUT_NAME:
        fname = Writer.Config.OPTIONAL_OUTPUT_NAME

    md_path = f"{fname}.md"
    json_path = f"{fname}.json"

    logger.Log("Saving story to disk", 3)
    output_md = _format_markdown(
        stats, title, story_body, outline, timeline_data, opts.build_timeline
    )
    logger.SaveStory(output_md)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(output_md)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(story_info, f, indent=4, ensure_ascii=False)

    export_paths = {}
    if opts.export_pdf:
        pdf_path = f"{fname}.pdf"
        export_pdf(title, story_body, pdf_path, summary=summary)
        export_paths["pdf"] = pdf_path
        logger.Log(f"PDF exported to {pdf_path}", 3)

    if opts.export_epub:
        epub_path = f"{fname}.epub"
        export_epub(title, story_body, epub_path, summary=summary, tags=tags)
        export_paths["epub"] = epub_path
        logger.Log(f"EPUB exported to {epub_path}", 3)

    record_story(
        title=title,
        summary=summary,
        tags=tags,
        word_count=total_words,
        md_path=md_path,
        json_path=json_path,
        elapsed_seconds=elapsed,
        models_used={
            "outline": Writer.Config.INITIAL_OUTLINE_WRITER_MODEL,
            "chapter": Writer.Config.CHAPTER_STAGE1_WRITER_MODEL,
        },
        extra={
            "exports": export_paths,
            "character_builder": opts.character_builder,
            "world_builder": opts.world_builder,
        },
    )

    logger.Log(f"Story complete — {total_words} words in {elapsed:.1f}s", 4)
    return {
        "title": title,
        "summary": summary,
        "tags": tags,
        "word_count": total_words,
        "elapsed": elapsed,
        "md_path": md_path,
        "json_path": json_path,
        "exports": export_paths,
    }


def _build_stats_string(title, summary, tags, total_words, elapsed, base_prompt):
    return (
        f"Work Statistics:\n"
        f" - Total Words: {total_words}\n"
        f" - Title: {title}\n"
        f" - Summary: {summary}\n"
        f" - Tags: {tags}\n"
        f" - Generation Date: {datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n"
        f" - Generation Time: {elapsed:.1f}s\n"
        f" - Average WPM: {60 * (total_words / elapsed) if elapsed else 0:.0f}\n"
        f"\nUser Settings:\n"
        f" - Base Prompt: {base_prompt}\n"
        f"\nGeneration Settings:\n"
        f" - Generator: {GENERATOR_ID}\n"
        f" - Outline Model: {Writer.Config.INITIAL_OUTLINE_WRITER_MODEL}\n"
        f" - Chapter Outline Model: {Writer.Config.CHAPTER_OUTLINE_WRITER_MODEL}\n"
        f" - Chapter Stage 1 Model: {Writer.Config.CHAPTER_STAGE1_WRITER_MODEL}\n"
        f" - Chapter Stage 2 Model: {Writer.Config.CHAPTER_STAGE2_WRITER_MODEL}\n"
        f" - Chapter Stage 3 Model: {Writer.Config.CHAPTER_STAGE3_WRITER_MODEL}\n"
        f" - Chapter Stage 4 Model: {Writer.Config.CHAPTER_STAGE4_WRITER_MODEL}\n"
        f" - Revision Model: {Writer.Config.REVISION_MODEL}\n"
        f" - Seed: {Writer.Config.SEED}\n"
    )


def _format_markdown(stats, title, body, outline, timeline_data, include_timeline):
    parts = [
        stats,
        "\n---\n",
        f"# {title}\n",
        body,
        "\n---\n# Outline\n```\n",
        outline,
        "\n```\n",
    ]
    if include_timeline and timeline_data:
        parts.extend(["\n---\n", format_timeline_markdown(timeline_data), "\n"])
    return "".join(parts)
