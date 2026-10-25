# Software thumbnails

The software page uses a coordinated set of editable TikZ miniatures, adapted
from the original talk and research figures. Each diagram emphasizes a single
mechanism at thumbnail scale: causal pathways, distributional comparison,
policy improvement, kernel approximation, or representation learning.

`miniatures/style.tex` defines the shared sans-serif typography, line weights,
and blue, green, orange, and red palette used throughout the research figures.
Geometry has a subtle three-degree tilt; text and the outer frame stay upright.
Every image uses the same 720 × 440 canvas, with a short mechanism caption.

Most miniatures are conceptual redraws. The risk curves, effect curves,
uncertainty regions, embedding positions, and selected tree path are schematic.
The interpretable DTE miniature is an exception: it uses the saved experimental
surfaces and exact selected locations, as described below.
In the architecture miniatures, repeated pair/loss
annotations are omitted; ALAD's extra consistency checks appear as round trips.
Detailed notes are also included beside the geometry in each TeX source.

Rebuild from the repository root:

```sh
python3 _software_thumbnails/build.py
```

Requires `pdflatex`, Poppler's `pdftoppm`, and ImageMagick's `magick`, as do the
existing research-figure builders. No extra Python packages are needed.
TeX compilation happens in a temporary directory. `figures.json` points to the
current editable miniatures. `original-figures.json` preserves the source and
crop references used for the first set of direct figure exports (one-based PDF
pages and PDF points measured from the top left). The underscore-prefixed source
directory is not included in the Jekyll site.

## Original references

| Miniature | Original figure |
| --- | --- |
| med_bench | `mediation_graph.pdf` from the mediation-analysis project: the standard treatment–mediator–outcome graph with covariates. |
| Interpretable distributional treatment effects | The two location-learning experiments from `interpretable-dr-me-test/results/location_explainer/figure_data.npz`, matching the contour figure in the NeurIPS manuscript and Interventional Mean Embeddings talk. Saved numerical data and metadata are retained in `sources/interpretable-dte-*`. |
| adaptive-KTE | `figures/mean-embedding-final.tex` from the Interventional Mean Embeddings talk in `Work/Talks/Interventional-Mean-Embeddings/6acc0abee20d1f6fe9b3384a`. The two-laws/MMD illustration is used as a conceptual treatment-effect testing visual, not an adaptive experiment result. Copied as `sources/treatment-effects.tex`. |
| Counterfactual policy mean embeddings | Final diagram from `gifs/mean_embedding_frames.tex`; the miniature retains the law-to-embedding mapping with fewer labels. |
| Continuous-treatment mediation | `images/mediation_aistats.pdf` from the *Causal Mediation – Houssam* paper sources, copied as `sources/continuous-mediation.pdf`. The new miniature combines the direct/mediated paths with a schematic dose-dependent effect curve; covariate-adjustment edges are omitted for space. |
| Sequential CRM | `scrm/gaussian_example/gaussian_sequential_crm.pdf` referenced by `Slides___SCRM___Gatsby/presentation.tex`, copied as `sources/gaussian-sequential-crm.pdf`. |
| Efficient Kernel UCB | Nyström feature projection, page 10 of the January 2022 Thoth talk (T05). |
| Nested bandits | `nested/tree.png` referenced by the Gatsby talk source; also shown on page 6 of the ICML 2022 talk (T06). Copied as `sources/nested-bandits-tree.png`. |
| Continuous-action CRM | `image/proximal_toy.pdf` referenced by the Gatsby talk source; also shown on page 7 of the ICLR 2020 workshop talk (T03). Copied as `sources/continuous-crm-proximal.pdf`. |
| ALAD | Architecture diagram, page 8 of the ICDM 2018 talk (T02). |
| Efficient GAN anomaly detection | Inference architecture, page 13 of the 2018 Deep Learning 2.0 talk (T01). |

External sources were copied from the author's local talk and paper archives.
Only the individual figures needed for rebuilding are retained here; the slide
PDFs already present under `assets/slides/` are reused directly.

## Interpretable DTE experiment

The two panels preserve the joint estimated doubly robust training criterion
on the original grid, using a shared absolute colour scale. Green shading is
this criterion, not a density, witness height, p-value, or individual effect.
The orange cross is the fixed first location; the blue star is the second
location selected by grid maximization:

| Panel | Fixed v1 | Learned v2 |
| --- | --- | --- |
| Central v1 | (0, −0.05) | (−2.025, −0.1181818…) |
| Left v1 | (−1.8, −0.06) | (0.45, 0.1181818…) |

The score divides the original plotted objective by the training sample size
(1375), which leaves the maximizers unchanged. Oracle markers, outcome clouds,
numeric ticks, and the colour bar are omitted for legibility. The two plots have
a slight opposite tilt, with upright labels. They do not show joint optimization
of both locations or results from the held-out test.

`export_dte_contours.py` converts the retained NumPy archive into the checked-in
`miniatures/interpretable-dte-contours.tex`. Running this optional export requires
NumPy and Matplotlib; the normal thumbnail build uses only the generated TeX.
The archive and metadata come from the author's local `interpretable-dr-me-test`
repository, generated by `illustrate_dr_me_locations.py` using the original
`contour_estimated_oracle.py` numerical routines. Source hashes and experiment
parameters are recorded in `sources/interpretable-dte-metadata.json`.
