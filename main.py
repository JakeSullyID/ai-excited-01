"""Copy the held image to the output directory byte-for-byte."""
# This module automates transferring the stored visual asset to the target location.
import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    src = os.path.join(os.path.dirname(__file__), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    # Execution triggers replication of the picture to the destination path.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
