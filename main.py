"""ai-excited-01 entry: copy the entry image to the output directory.

The entry is the phoenix image in entry.png beside this file (1024x1024
PNG). This program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png, creating the output directory if needed.
No network, no randomness, no timestamps: two runs produce
byte-identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    # The grader sets MAKEFUN_OUTPUT_DIR to /output; locally it defaults
    # to ./out so `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
    # reproduces the graded run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
