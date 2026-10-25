#!/usr/bin/env python3
"""Render the software miniatures from their original figures and TeX sources."""

import json
from pathlib import Path
import shutil
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = ROOT / "assets/img/software"


def run(*args, cwd=None):
    return subprocess.run(
        [str(arg) for arg in args], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd,
    ).stdout


def main():
    for tool in ("pdflatex", "pdftoppm", "magick"):
        if not shutil.which(tool):
            raise SystemExit(f"Missing dependency: {tool}")
    figures = json.loads((HERE / "figures.json").read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="software-thumbnails-") as temporary:
        work = Path(temporary)
        for figure in figures:
            source = ROOT / figure["source"]
            name = figure["name"]
            if source.suffix == ".tex":
                run("pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    f"-output-directory={work}", source, cwd=source.parent)
                source = work / f"{source.stem}.pdf"

            if source.suffix == ".pdf":
                page = str(figure.get("page", 1))
                command = ["pdftoppm", "-f", page, "-l", page,
                           "-r", "360", "-singlefile", "-png"]
                if figure.get("crop"):
                    # Crop coordinates are PDF points measured from top left.
                    left, top, right, bottom = figure["crop"]
                    command += ["-x", round(left * 5), "-y", round(top * 5),
                                "-W", round((right - left) * 5),
                                "-H", round((bottom - top) * 5)]
                run(*command, source, work / name)
                source = work / f"{name}.png"

            destination = OUTPUT / f"{name}.png"
            command = ["magick", source, "-background", "white",
                       "-alpha", "remove", "-alpha", "off"]
            if figure.get("trim"):
                command += ["-trim", "+repage"]
            size = "720x440!" if figure.get("native_canvas") else "664x384"
            run(*command, "-resize", size, "-gravity", "center",
                "-extent", "720x440", "-strip", destination)
            dimensions = run("magick", "identify", "-format", "%wx%h", destination)
            if dimensions != b"720x440":
                raise ValueError(f"Unexpected dimensions for {name}: {dimensions!r}")
            print(f"Built {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stdout.decode(errors="replace")) from error
