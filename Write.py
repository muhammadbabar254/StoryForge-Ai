#!/usr/bin/env python3
"""
StoryForge AI — legacy CLI entry point.

This script is maintained for backward compatibility.
Prefer: python forge.py -Prompt <path>
"""

import sys
import warnings

warnings.warn(
    "Write.py is deprecated. Use 'python forge.py' instead.",
    DeprecationWarning,
    stacklevel=1,
)

from storyforge.cli import main

if __name__ == "__main__":
    sys.exit(main())
