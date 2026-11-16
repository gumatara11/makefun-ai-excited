import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
