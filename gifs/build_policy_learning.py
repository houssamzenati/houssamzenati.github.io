#!/usr/bin/env python3
"""Rebuild the learning animation with TeX, Poppler, and ImageMagick."""

import shutil
import subprocess
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAME = "policy_learning"
# Hundredths of a second: hold the initial rule, follow the policy trajectory,
# then pause before the illustration restarts.
DELAYS = [70] + [8] * 59 + [160]


def run(*args):
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    for tool in ("pdflatex", "pdftoppm", "magick"):
        if not shutil.which(tool):
            raise SystemExit(f"Missing dependency: {tool}")

    with tempfile.TemporaryDirectory(prefix=f"{NAME}-") as temporary:
        work = Path(temporary)
        source = HERE / f"{NAME}_frames.tex"
        pdf = work / f"{NAME}_frames.pdf"
        try:
            run("pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                f"-output-directory={work}", str(source))
            run("pdftoppm", "-png", "-scale-to-x", "1800", "-scale-to-y", "-1",
                str(pdf), str(work / "frame"))
            frames = sorted(work.glob("frame-*.png"))
            if len(frames) != len(DELAYS):
                raise ValueError(f"Expected {len(DELAYS)} frames, found {len(frames)}")

            # The complete final frame contains all stage colors. Sharing its
            # palette prevents color flicker without quantizing a large montage.
            palette = work / "palette.png"
            run("magick", str(frames[-1]),
                "-colors", "128", "-unique-colors", str(palette))
            command = ["magick"]
            for frame, delay in zip(frames, DELAYS):
                command.extend(["-delay", str(delay), str(frame)])
            # Keep opaque full frames: layer optimization merges the white
            # canvas with the pale policy region in some ImageMagick versions.
            command.extend(["+dither", "-remap", str(palette),
                            "-loop", "0",
                            str(work / f"{NAME}.gif")])
            run(*command)
        except subprocess.CalledProcessError as error:
            raise SystemExit(error.stdout.decode(errors="replace")) from error

        shutil.copy2(pdf, HERE / pdf.name)
        shutil.copy2(work / f"{NAME}.gif", HERE / f"{NAME}.gif")
        shutil.copy2(frames[-1], HERE / f"{NAME}_final_slide.png")
    print(f"Built {len(DELAYS)} frames, {sum(DELAYS) / 100:g} seconds.")


if __name__ == "__main__":
    main()
