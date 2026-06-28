"""Story Timeline — tracks narrative events across chapters for consistency."""

import json

import Writer.Config
import Writer.Prompts

TIMELINE_PROMPT = """
Analyze the following story chapters and create a structured timeline of key narrative events.

<TITLE>{title}</TITLE>

<OUTLINE>
{outline}
</OUTLINE>

<CHAPTERS>
{chapters}
</CHAPTERS>

Respond with ONLY valid JSON:
{{
  "timeline": [
    {{
      "chapter": 1,
      "event_order": 1,
      "event": "Brief description of what happens",
      "characters_involved": ["Name1", "Name2"],
      "location": "Where it happens",
      "time_marker": "When (relative or absolute)",
      "significance": "Why this event matters to the plot",
      "emotional_tone": "mood of the scene"
    }}
  ],
  "plot_threads": [
    {{
      "thread_name": "Main conflict or subplot name",
      "introduced_chapter": 1,
      "resolved_chapter": null,
      "status": "open|resolved|ongoing"
    }}
  ]
}}
"""


def build_timeline(
    Interface, logger, title: str, outline: str, chapters: list[str]
) -> dict:
    """Generate a structured story timeline from completed chapters."""
    chapter_text = "\n\n".join(chapters)
    if len(chapter_text) > 12000:
        chapter_text = chapter_text[:12000] + "\n\n[... truncated for timeline analysis ...]"

    messages = [
        Interface.BuildSystemQuery(Writer.Prompts.DEFAULT_SYSTEM_PROMPT),
        Interface.BuildUserQuery(
            TIMELINE_PROMPT.format(
                title=title, outline=outline, chapters=chapter_text
            )
        ),
    ]
    messages = Interface.SafeGenerateText(
        logger, messages, Writer.Config.INFO_MODEL, _MinWordCount=100
    )
    raw = Interface.GetLastMessageText(messages)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        return json.loads(raw[start:end])
    except (json.JSONDecodeError, ValueError):
        logger.Log("Timeline JSON parse failed — returning empty timeline", 6)
        return {"timeline": [], "plot_threads": [], "raw": raw}


def format_timeline_markdown(timeline_data: dict) -> str:
    """Render timeline as readable markdown."""
    lines = ["# Story Timeline\n"]
    for event in timeline_data.get("timeline", []):
        ch = event.get("chapter", "?")
        lines.append(
            f"- **Ch.{ch}** — {event.get('event', '')} "
            f"*{event.get('location', '')}* ({event.get('emotional_tone', '')})"
        )
    if timeline_data.get("plot_threads"):
        lines.append("\n## Plot Threads\n")
        for thread in timeline_data["plot_threads"]:
            status = thread.get("status", "unknown")
            lines.append(
                f"- **{thread.get('thread_name', '?')}** [{status}] "
                f"(Ch.{thread.get('introduced_chapter', '?')})"
            )
    return "\n".join(lines)
