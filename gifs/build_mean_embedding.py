#!/usr/bin/env python3
"""Rebuild the distributional inference animation with TeX and ImageMagick."""

import shutil
import subprocess
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAME = "mean_embedding"
WIDTH = 1800
# Hundredths of a second: reveal the two mappings on one fixed diagram,
# then hold the complete embedding operation.
DELAYS = [110, 100, 380]


def run(*args):
    return subprocess.run(
        args, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout


def validate_gif(path):
    """Check the displayed frames after reversing GIF layer optimization."""
    output = run("magick", str(path), "-coalesce", "-format", "%w %h %T\n", "info:")
    metadata = [tuple(map(int, line.split())) for line in output.decode().splitlines()]
    if len(metadata) != len(DELAYS):
        raise ValueError(f"Expected {len(DELAYS)} GIF frames, found {len(metadata)}")
    dimensions = {(width, height) for width, height, _ in metadata}
    if len(dimensions) != 1 or metadata[0][0] != WIDTH:
        raise ValueError(f"Unexpected coalesced GIF dimensions: {dimensions}")
    actual_delays = [delay for _, _, delay in metadata]
    if actual_delays != DELAYS:
        raise ValueError(f"Unexpected GIF delays: {actual_delays}")


def main():
    for tool in ("pdflatex", "pdftoppm", "magick"):
        if not shutil.which(tool):
            raise SystemExit(f"Missing dependency: {tool}")

    with tempfile.TemporaryDirectory(prefix=f"{NAME}-") as temporary:
        work = Path(temporary)
        source = HERE / f"{NAME}_frames.tex"
        pdf = work / f"{NAME}_frames.pdf"
        gif = work / f"{NAME}.gif"
        try:
            run("pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                f"-output-directory={work}", str(source))
            run("pdftoppm", "-png", "-scale-to-x", str(WIDTH), "-scale-to-y", "-1",
                str(pdf), str(work / "frame"))
            frames = sorted(
                work.glob("frame-*.png"),
                key=lambda path: int(path.stem.rsplit("-", 1)[1]),
            )
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
            command.extend(["+dither", "-remap", str(palette),
                            "-loop", "0", "-layers", "Optimize", str(gif)])
            run(*command)
            validate_gif(gif)
        except subprocess.CalledProcessError as error:
            raise SystemExit(error.stdout.decode(errors="replace")) from error

        shutil.copy2(pdf, HERE / pdf.name)
        shutil.copy2(gif, HERE / gif.name)
        shutil.copy2(frames[-1], HERE / f"{NAME}_final_slide.png")
    print(f"Built and validated {len(DELAYS)} frames, {sum(DELAYS) / 100:g} seconds.")


if __name__ == "__main__":
    main()
