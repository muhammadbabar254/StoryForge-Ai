"""StoryForge AI branding constants and terminal display helpers."""

from storyforge.__version__ import __author__, __github__, __linkedin__, __url__, __version__

APP_NAME = "StoryForge AI"
APP_TAGLINE = "Forge compelling novels with intelligent AI storytelling"
GENERATOR_ID = f"StoryForge_AI_{__version__.replace('.', '-')}"

BANNER = f"""
╔══════════════════════════════════════════════════════════════╗
║   ⚔  {APP_NAME} v{__version__:<43}║
║   {APP_TAGLINE:<58}║
║   Author: {__author__:<49}║
║   {__url__:<58}║
╚══════════════════════════════════════════════════════════════╝
"""


def print_banner():
    try:
        import termcolor
        print(termcolor.colored(BANNER, "cyan"))
    except ImportError:
        print(BANNER)
