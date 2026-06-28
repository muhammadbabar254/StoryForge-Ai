"""Character Builder — generates structured character profiles for story consistency."""

import json
from typing import List, Optional

import Writer.Config
import Writer.Prompts

CHARACTER_BUILDER_PROMPT = """
You are a master character designer for StoryForge AI. Based on the story prompt below, create
detailed character profiles that will maintain consistency throughout a full-length novel.

<PROMPT>
{prompt}
</PROMPT>

{existing_characters}

Respond with ONLY valid JSON in this exact structure:
{{
  "characters": [
    {{
      "name": "Character Name",
      "role": "protagonist|antagonist|supporting|minor",
      "age": "approximate age or range",
      "physical_description": "detailed appearance",
      "personality": "traits, quirks, speech patterns",
      "background": "history and formative events",
      "motivation": "what drives them",
      "goals": "what they want to achieve",
      "fears": "what they fear losing or facing",
      "relationships": [
        {{"with": "Other Character", "dynamic": "description of relationship"}}
      ],
      "character_arc": "how they change from beginning to end",
      "voice_notes": "how they speak — vocabulary, tone, verbal tics"
    }}
  ]
}}

Create at least 2 main characters and 3-5 supporting characters. Be specific and creative.
"""


def build_characters(Interface, logger, prompt: str, existing: Optional[List] = None) -> dict:
    """Generate structured character profiles from a story prompt."""
    existing_block = ""
    if existing:
        existing_block = (
            "Expand upon these existing characters:\n"
            + json.dumps(existing, indent=2)
        )

    messages = [
        Interface.BuildSystemQuery(Writer.Prompts.DEFAULT_SYSTEM_PROMPT),
        Interface.BuildUserQuery(
            CHARACTER_BUILDER_PROMPT.format(
                prompt=prompt, existing_characters=existing_block
            )
        ),
    ]
    messages = Interface.SafeGenerateText(
        logger, messages, Writer.Config.INITIAL_OUTLINE_WRITER_MODEL, _MinWordCount=200
    )
    raw = Interface.GetLastMessageText(messages)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        return json.loads(raw[start:end])
    except (json.JSONDecodeError, ValueError):
        logger.Log("Character Builder JSON parse failed — returning raw text", 6)
        return {"characters": [], "raw": raw}


def format_for_prompt(character_data: dict) -> str:
    """Format character profiles as markdown for injection into outline prompts."""
    if not character_data.get("characters"):
        return character_data.get("raw", "")

    lines = ["# Character Profiles (StoryForge Character Builder)\n"]
    for char in character_data["characters"]:
        lines.append(f"## {char.get('name', 'Unknown')} ({char.get('role', 'unknown')})")
        for key in (
            "physical_description",
            "personality",
            "background",
            "motivation",
            "goals",
            "fears",
            "character_arc",
            "voice_notes",
        ):
            if char.get(key):
                label = key.replace("_", " ").title()
                lines.append(f"- **{label}**: {char[key]}")
        if char.get("relationships"):
            lines.append("- **Relationships**:")
            for rel in char["relationships"]:
                lines.append(f"  - {rel.get('with', '?')}: {rel.get('dynamic', '')}")
        lines.append("")
    return "\n".join(lines)
