#!/usr/bin/env python3
"""Build one schematic trajectory of a history-dependent experiment."""

import math
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "adaptive_inference"
DELAYS = [90] + ([110, 90] + [12] * 5 + [100]) * 3 + [250]
GRID = [-3 + 6 * i / 160 for i in range(161)]
UNCERTAINTY_SCALE = 1.2
# A schematic realized path, not an acquisition rule or algorithm simulation.
# Keeping these actions preserves the previously illustrated curve updates.
# The first three actions produce outcomes; the last is the next assignment.
ASSIGNMENTS = [1.275, -0.1875, 2.0625, 3.0]


def run(*args, cwd=None):
    subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT)


def kernel(x, z):
    return math.exp(-0.5 * ((x - z) / 1.25) ** 2)


def forward(lower, values):
    result = []
    for i, value in enumerate(values):
        result.append((value - sum(lower[i][j] * result[j]
                                   for j in range(i))) / lower[i][i])
    return result


def posterior(xs, ys):
    """Small GP regression with a fixed kernel and observation-noise SD .08."""
    count = len(xs)
    lower = [[0.0] * count for _ in xs]
    for i in range(count):
        for j in range(i + 1):
            value = kernel(xs[i], xs[j]) + (0.08 ** 2 if i == j else 0)
            value -= sum(lower[i][k] * lower[j][k] for k in range(j))
            lower[i][j] = math.sqrt(max(value, 1e-12)) if i == j else value / lower[j][j]
    transformed_y = forward(lower, ys)
    means, deviations = [], []
    for x in GRID:
        transformed_k = forward(lower, [kernel(x, z) for z in xs])
        means.append(sum(a * b for a, b in zip(transformed_k, transformed_y)))
        deviations.append(math.sqrt(max(1 - sum(v * v for v in transformed_k), 1e-10)))
    return means, deviations


def mean_outcome(x):
    return 0.78 * math.tanh(1.1 * (x - 0.55)) + 0.08 * math.sin(2 * x)


def canvas(x, y):
    return 2.1 + (x + 3) * 14.5 / 6, 3.35 + 1.28 * y


def coordinates(values):
    return " ".join(f"({a:.4f},{b:.4f})"
                    for a, b in (canvas(x, y) for x, y in zip(GRID, values)))


def draw_frame(mean, deviation, xs, ys, query=None, stage=None):
    upper = [m + UNCERTAINTY_SCALE * s for m, s in zip(mean, deviation)]
    lower = [m - UNCERTAINTY_SCALE * s for m, s in zip(mean, deviation)]
    reverse_lower = " ".join(f"({a:.4f},{b:.4f})"
                            for a, b in reversed([canvas(x, y)
                                                  for x, y in zip(GRID, lower)]))
    lines = [
        r"\begin{scope}",
        r"\clip (1.91,1.12) rectangle (16.8,6.3);",
        r"\fill[green!12] plot coordinates {" + coordinates(upper) +
        r"} -- plot coordinates {" + reverse_lower + r"} -- cycle;",
        r"\draw[blue!65,line width=1.15pt] plot coordinates {" + coordinates(mean) + "};",
    ]
    for index, (x, y) in enumerate(zip(xs, ys)):
        px, py = canvas(x, y)
        if index == len(xs) - 1:
            lines.append(rf"\fill[blue!15] ({px:.4f},{py:.4f}) circle (5pt);")
            lines.append(rf"\fill[blue!80] ({px:.4f},{py:.4f}) circle (2.7pt);")
        else:
            lines.append(rf"\fill[blue!65,opacity=.75] ({px:.4f},{py:.4f}) circle (2.7pt);")
    lines.append(r"\end{scope}")
    if query is not None:
        # An assignment has no observed outcome yet: mark it on the x-axis.
        # The guide reaches only the current prediction, not the band edge.
        query_index = min(range(len(GRID)), key=lambda i: abs(GRID[i] - query))
        px, py = canvas(query, mean[query_index])
        anchor, offset = ("east", -.18) if px > 12.5 else ("west", .18)
        lines += [
            rf"\draw[orange!55,densely dashed,line width=.75pt] ({px:.4f},1.27) -- ({px:.4f},{py:.4f});",
            rf"\draw[orange!55,line width=1.5pt,fill=white] ({px:.4f},1.1) circle (.145);",
            rf"\node[anchor={anchor},text=black!75,font=\fontsize{{12}}{{15}}\selectfont,fill=white,inner sep=2pt] at ({px+offset:.4f},1.5) {{Next assignment $A_{{t+1}}$}};",
        ]
    elif stage is not None:
        px, py = canvas(xs[-1], ys[-1])
        side = -1 if px > 12.5 else 1
        anchor = "east" if side < 0 else "west"
        label_y = min(py - .85, 2.65)
        lines += [
            rf"\draw[black!35,line width=.85pt] ({px+side*.14:.4f},{py-.17:.4f}) -- ({px+side*.36:.4f},{label_y+.18:.4f});",
            rf"\node[anchor={anchor},text=black!75,font=\fontsize{{12}}{{15}}\selectfont,fill=white,inner sep=2pt] at ({px+side*.42:.4f},{label_y:.4f}) {{New outcome}};",
        ]
    return "\n".join(lines)


def build_data():
    xs = [-2.7, 2.7]
    ys = [mean_outcome(x) for x in xs]
    mean, deviation = posterior(xs, ys)
    frames = [draw_frame(mean, deviation, xs, ys, None)]
    for query in ASSIGNMENTS[:-1]:
        frames.append(draw_frame(mean, deviation, xs, ys, query))
        xs = xs + [query]
        ys = ys + [mean_outcome(query)]
        # Show the new measurement against the OLD estimate first. This pause
        # makes the cause of the later curve movement explicit.
        frames.append(draw_frame(mean, deviation, xs, ys, stage="observe"))
        new_mean, new_deviation = posterior(xs, ys)
        for step in range(1, 6):
            amount = step / 5
            # Smooth display transition between fitted models.
            means = [a + amount * (b - a) for a, b in zip(mean, new_mean)]
            deviations = [a + amount * (b - a)
                          for a, b in zip(deviation, new_deviation)]
            frames.append(draw_frame(means, deviations, xs, ys, stage="update"))
        mean, deviation = new_mean, new_deviation
        frames.append(draw_frame(mean, deviation, xs, ys, stage="updated"))
    frames.append(draw_frame(mean, deviation, xs, ys, ASSIGNMENTS[-1]))
    return (r"\newcommand{\responsedata}[1]{\ifcase#1" + "\n" +
            "\n".join("\\or\n" + frame for frame in frames) + "\n\\fi}\n")


def main():
    for tool in ("pdflatex", "pdftoppm", "magick"):
        if not shutil.which(tool):
            raise SystemExit(f"Missing dependency: {tool}")
    with tempfile.TemporaryDirectory(prefix=f"{NAME}-") as temporary:
        work = Path(temporary)
        pdf = work / f"{NAME}_frames.pdf"
        (work / f"{NAME}_data.tex").write_text(build_data())
        try:
            run("pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                f"-output-directory={work}", str(HERE / f"{NAME}_frames.tex"), cwd=work)
            run("pdftoppm", "-png", "-scale-to-x", "1800", "-scale-to-y", "700",
                str(pdf), str(work / "frame"))
            frames = sorted(work.glob("frame-*.png"))
            if len(frames) != len(DELAYS):
                raise ValueError(f"Expected {len(DELAYS)} frames, found {len(frames)}")
            palette = work / "palette.png"
            run("magick", *(str(frame) for frame in frames),
                "-append", "-colors", "128", "-unique-colors", str(palette))
            command = ["magick"]
            for frame, delay in zip(frames, DELAYS):
                command.extend(["-delay", str(delay), str(frame)])
            command.extend(["+dither", "-remap", str(palette), "-loop", "0",
                            "-layers", "Optimize", str(work / f"{NAME}.gif")])
            run(*command)
        except subprocess.CalledProcessError as error:
            raise SystemExit(error.stdout.decode(errors="replace")) from error
        shutil.copy2(pdf, HERE / pdf.name)
        shutil.copy2(work / f"{NAME}.gif", HERE / f"{NAME}.gif")
        shutil.copy2(frames[-1], HERE / f"{NAME}_final_slide.png")
    print(f"Built {len(DELAYS)} frames, {sum(DELAYS) / 100:g} seconds.")


if __name__ == "__main__":
    main()
