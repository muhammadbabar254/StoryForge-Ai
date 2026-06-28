"""StoryForge AI — command-line interface."""

import argparse
import sys

import Writer.Config

from storyforge.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="forge",
        description="StoryForge AI — Generate full-length novels with AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python forge.py -Prompt prompts/example.txt\n"
            "  python forge.py -Prompt prompts/example.txt -CharacterBuilder -WorldBuilder\n"
            "  python forge.py -Prompt prompts/example.txt -ExportPDF -ExportEPUB\n"
            "\nStoryForge AI by Muhammad Babar — https://babar.site.je"
        ),
    )

    parser.add_argument("-Prompt", help="Path to file containing the story prompt")
    parser.add_argument(
        "-Output", default="", type=str, help="Optional output file path (without extension)"
    )
    parser.add_argument(
        "-InitialOutlineModel",
        default=Writer.Config.INITIAL_OUTLINE_WRITER_MODEL,
        type=str,
        help="Model for the base outline",
    )
    parser.add_argument(
        "-ChapterOutlineModel",
        default=Writer.Config.CHAPTER_OUTLINE_WRITER_MODEL,
        type=str,
        help="Model for per-chapter outlines",
    )
    parser.add_argument(
        "-ChapterS1Model",
        default=Writer.Config.CHAPTER_STAGE1_WRITER_MODEL,
        type=str,
        help="Chapter writer stage 1 (plot)",
    )
    parser.add_argument(
        "-ChapterS2Model",
        default=Writer.Config.CHAPTER_STAGE2_WRITER_MODEL,
        type=str,
        help="Chapter writer stage 2 (character development)",
    )
    parser.add_argument(
        "-ChapterS3Model",
        default=Writer.Config.CHAPTER_STAGE3_WRITER_MODEL,
        type=str,
        help="Chapter writer stage 3 (dialogue)",
    )
    parser.add_argument(
        "-ChapterS4Model",
        default=Writer.Config.CHAPTER_STAGE4_WRITER_MODEL,
        type=str,
        help="Chapter writer stage 4 (final polish)",
    )
    parser.add_argument(
        "-ChapterRevisionModel",
        default=Writer.Config.CHAPTER_REVISION_WRITER_MODEL,
        type=str,
        help="Model for chapter revisions",
    )
    parser.add_argument(
        "-RevisionModel",
        default=Writer.Config.REVISION_MODEL,
        type=str,
        help="Model for constructive criticism",
    )
    parser.add_argument(
        "-EvalModel",
        default=Writer.Config.EVAL_MODEL,
        type=str,
        help="Model for quality evaluation",
    )
    parser.add_argument(
        "-InfoModel",
        default=Writer.Config.INFO_MODEL,
        type=str,
        help="Model for title/summary generation",
    )
    parser.add_argument(
        "-ScrubModel",
        default=Writer.Config.SCRUB_MODEL,
        type=str,
        help="Model for final story scrubbing",
    )
    parser.add_argument(
        "-CheckerModel",
        default=Writer.Config.CHECKER_MODEL,
        type=str,
        help="Model for output validation",
    )
    parser.add_argument(
        "-TranslatorModel",
        default=Writer.Config.TRANSLATOR_MODEL,
        type=str,
        help="Model for translation",
    )
    parser.add_argument(
        "-Translate", default="", type=str, help="Translate story to this language"
    )
    parser.add_argument(
        "-TranslatePrompt",
        default="",
        type=str,
        help="Translate input prompt to this language",
    )
    parser.add_argument("-Seed", default=12, type=int, help="Random seed for models")
    parser.add_argument(
        "-OutlineMinRevisions", default=0, type=int, help="Min outline revision passes"
    )
    parser.add_argument(
        "-OutlineMaxRevisions", default=3, type=int, help="Max outline revision passes"
    )
    parser.add_argument(
        "-ChapterMinRevisions", default=0, type=int, help="Min chapter revision passes"
    )
    parser.add_argument(
        "-ChapterMaxRevisions", default=3, type=int, help="Max chapter revision passes"
    )
    parser.add_argument(
        "-NoChapterRevision", action="store_true", help="Disable chapter revisions"
    )
    parser.add_argument(
        "-NoScrubChapters", action="store_true", help="Skip final scrub pass"
    )
    parser.add_argument(
        "-ExpandOutline",
        action="store_true",
        default=True,
        help="Expand outline chapter-by-chapter before writing",
    )
    parser.add_argument(
        "-EnableFinalEditPass",
        action="store_true",
        help="Run a final edit pass on the whole story",
    )
    parser.add_argument(
        "-Debug", action="store_true", help="Print system prompts during generation"
    )
    parser.add_argument(
        "-SceneGenerationPipeline",
        action="store_true",
        default=True,
        help="Use scene-by-scene generation pipeline",
    )

    # StoryForge feature flags
    parser.add_argument(
        "-CharacterBuilder",
        action="store_true",
        help="Run StoryForge Character Builder before outline generation",
    )
    parser.add_argument(
        "-WorldBuilder",
        action="store_true",
        help="Run StoryForge World Builder before outline generation",
    )
    parser.add_argument(
        "-BuildTimeline",
        action="store_true",
        default=True,
        help="Generate a story timeline after writing (default: on)",
    )
    parser.add_argument(
        "-NoTimeline", action="store_true", help="Skip timeline generation"
    )
    parser.add_argument(
        "-ExportPDF", action="store_true", help="Export story as PDF"
    )
    parser.add_argument(
        "-ExportEPUB", action="store_true", help="Export story as EPUB"
    )
    parser.add_argument(
        "-NoBanner", action="store_true", help="Suppress StoryForge startup banner"
    )

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.NoTimeline:
        args.BuildTimeline = False
    args.ShowBanner = not args.NoBanner

    try:
        result = run_pipeline(args)
        return 0 if result else 1
    except Exception as exc:
        print(f"StoryForge AI error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
