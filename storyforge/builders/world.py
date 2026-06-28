"""World Builder — generates structured world/setting profiles for story consistency."""

import json
from typing import Optional

import Writer.Config
import Writer.Prompts

WORLD_BUILDER_PROMPT = """
You are a master world-builder for StoryForge AI. Based on the story prompt below, create
a rich, internally consistent world that supports the narrative.

<PROMPT>
{prompt}
</PROMPT>

{existing_world}

Respond with ONLY valid JSON in this exact structure:
{{
  "world_name": "Name of the world/setting",
  "genre_context": "fantasy|sci-fi|contemporary|historical|etc",
  "time_period": "when the story takes place",
  "locations": [
    {{
      "name": "Location Name",
      "type": "city|region|building|planet|etc",
      "description": "sensory-rich description",
      "significance": "why this place matters to the plot",
      "mood": "atmospheric tone"
    }}
  ],
  "rules_and_systems": [
    {{
      "name": "Magic system / Technology / Social rule",
      "description": "how it works and its limits",
      "story_impact": "how it affects the plot"
    }}
  ],
  "culture": {{
    "values": "what the society values",
    "conflicts": "internal societal tensions",
    "customs": "notable traditions or norms"
  }},
  "history": "brief relevant backstory of the world",
  "atmosphere": "overall mood and tone of the setting"
}}
"""


def build_world(Interface, logger, prompt: str, existing: Optional[dict] = None) -> dict:
    """Generate structured world profile from a story prompt."""
    existing_block = ""
    if existing:
        existing_block = (
            "Expand upon this existing world:\n" + json.dumps(existing, indent=2)
        )

    messages = [
        Interface.BuildSystemQuery(Writer.Prompts.DEFAULT_SYSTEM_PROMPT),
        Interface.BuildUserQuery(
            WORLD_BUILDER_PROMPT.format(prompt=prompt, existing_world=existing_block)
        ),
    ]
    messages = Interface.SafeGenerateText(
        logger, messages, Writer.Config.INITIAL_OUTLINE_WRITER_MODEL, _MinWordCount=150
    )
    raw = Interface.GetLastMessageText(messages)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        return json.loads(raw[start:end])
    except (json.JSONDecodeError, ValueError):
        logger.Log("World Builder JSON parse failed — returning raw text", 6)
        return {"raw": raw}


def format_for_prompt(world_data: dict) -> str:
    """Format world profile as markdown for injection into outline prompts."""
    if world_data.get("raw") and not world_data.get("world_name"):
        return world_data["raw"]

    lines = ["# World Profile (StoryForge World Builder)\n"]
    if world_data.get("world_name"):
        lines.append(f"**World**: {world_data['world_name']}")
    for key in ("genre_context", "time_period", "atmosphere", "history"):
        if world_data.get(key):
            lines.append(f"**{key.replace('_', ' ').title()}**: {world_data[key]}")

    if world_data.get("locations"):
        lines.append("\n## Key Locations")
        for loc in world_data["locations"]:
            lines.append(f"### {loc.get('name', 'Unknown')}")
            for k in ("type", "description", "significance", "mood"):
                if loc.get(k):
                    lines.append(f"- **{k.title()}**: {loc[k]}")

    if world_data.get("rules_and_systems"):
        lines.append("\n## Rules & Systems")
        for rule in world_data["rules_and_systems"]:
            lines.append(f"### {rule.get('name', 'Rule')}")
            if rule.get("description"):
                lines.append(f"- {rule['description']}")
            if rule.get("story_impact"):
                lines.append(f"- *Story impact*: {rule['story_impact']}")

    if world_data.get("culture"):
        lines.append("\n## Culture")
        for k, v in world_data["culture"].items():
            lines.append(f"- **{k.title()}**: {v}")

    return "\n".join(lines)
