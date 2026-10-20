# Research animations

## Learning to intervene

Edit `policy_learning_frames.tex`, then run from the repository root:

```sh
python3 gifs/build_policy_learning.py
```

Requires `pdflatex` (with TikZ and Latin Modern), Poppler's `pdftoppm`, and
ImageMagick's `magick` on the executable search path. The script regenerates
the frame PDF, animated GIF, and static final slide without leaving build files.
Frame durations are specified in `DELAYS` in the script.

The animation preserves the original policy-space illustration. The moving
policy follows the exact gradient-flow orbit of the illustrative quadratic
`R(x,y) = 0.5 * ((x-5.75)/1.35)^2 + 0.5 * ((y-3.35)/0.78)^2`.
The three orange ellipses are level sets of that same objective. Starting at
`(1.45, 1.45)`, each centered coordinate decays exponentially with the inverse
squared scale of its corresponding risk axis; the flow stops at time `4.12`.
All constants are shared by the contour and trajectory definitions in the TeX
source. Smooth animation pacing across 61 frames reparameterizes the orbit.

The continuous curve suggests a policy flow; its marked samples suggest
successive policy updates. The moving point is labelled simply `pi`, so its
animation parameter does not imply a deployment counter. Offline updates can
reuse a fixed dataset.
The solid path learns an intervention rule from logged actions and outcomes.
Dashed edges add deployment and new feedback in the sequential setting.
Geometry and iterates are schematic, not an empirical convergence result or
an assertion that the research problems are quadratic or all the algorithms
follow this flow. The fixed blue halo highlights the current policy; it is not
a confidence set. The final iterate remains distinct from the optimum.

## Nuisance-robust inference

Edit `nuisance_robust_inference_frames.tex`, then run:

```sh
python3 gifs/build_nuisance_robust_inference.py
```

This produces a 49-frame animation, its frame PDF, and a static poster, using
the same dependencies as the other figures. One fixed diagram maps nearby
nuisance fits through orthogonal bias correction to a scalar target estimate.
The animation varies only the fitted functions; the observed data and target
remain fixed. There are no changes of scene or additional diagrams.
Short labels pair the nuisance and target notation with plain language,
without equations or a notation glossary. Colors follow the policy-learning
figure: blue fitted objects, a red target, pale green estimation, and neutral
text and axes. Opaque full GIF frames preserve these colors; the builder
checks the encoded final frame against the poster to catch color changes.

This is a local schematic of Neyman orthogonality, not a fitted model or a
numerical experiment. The displayed output has a quadratic perturbation term,
a small linear finite-sample term, and a fixed sampling offset. Orthogonality
holds for the population score at the truth, not exactly for an arbitrary
empirical estimator. A second-order population remainder also requires local
smoothness and identification in the target direction. The horizontal axes
have unrelated units, so movement sizes are qualitative. The faint curves
and points show nearby fits and their corresponding estimates, not confidence
regions. The constant blue halo highlights the current estimate and is not a
confidence region. Sampling error is not removed.

The Research page shows this figure as the general inference illustration.
Reference: [Double/Debiased Machine Learning](https://arxiv.org/abs/1608.00060).

## Kernel mean embedding

Edit `mean_embedding_frames.tex`, then run from the repository root:

```sh
python3 gifs/build_mean_embedding.py
```

Uses the same dependencies as the learning animation. The builder regenerates
the three-page frame PDF, animated GIF, and static final slide, and verifies
the GIF's dimensions and frame timings. This earlier distributional
illustration is retained as a separate editable asset.

One fixed diagram shows the kernel mean embedding operation. The original
example densities, `N(0, 0.6^2)` and `N(0.6, 1)`, map to two color-matched
points in a shared RKHS. The ellipse and point positions are schematic; they
are not a two-dimensional projection or a numerical distance computation.
The animation reveals the two mapping arrows, then holds the complete figure.

Reference: [CPME](https://arxiv.org/abs/2506.02793).

## Adaptive experimentation

Edit the appearance in `adaptive_inference_frames.tex` or the toy design in
`build_adaptive_inference.py`, then run from the repository root:

```sh
python3 gifs/build_adaptive_inference.py
```

The same TeX, Poppler, and ImageMagick dependencies regenerate the frame PDF,
animated GIF, and static final slide. No additional Python packages are needed.

One plot illustrates the common experimental model behind adaptive learning
and inference. The context is held fixed, the action coordinate is
one-dimensional, and outcomes are scalar. The x-axis is the assigned action;
the y-axis is the observed outcome. Blue dots are observations, the blue
curve estimates the conditional mean outcome, and the green band represents
model uncertainty.

The only displayed equation is the conditional observation-law factorization:
`p_{t+1}(a,y | H_t) = g_{t+1}(a | H_t) q_0(y | a)`.
The assignment rule `g` can depend on past observations `H_t`, while the
conditional outcome mechanism `q_0` is fixed. This is the no-context
specialization of the sequential model in
[Efficient Inference after Directionally Stable Adaptive Experiments](https://arxiv.org/abs/2602.21478),
and the expanded form of `O_{t+1} | H_t ~ P_0^{g_{t+1}}` in the research
statement's adaptive-experimentation section. The curve estimates
`m_0(a) = integral y q_0(y | a) dy`; this definition is kept out of the graphic
to avoid adding a second equation.

The orange ring marks the next assignment on the x-axis, before its outcome
is observed. Its guide reaches the current mean estimate, not an upper
confidence bound. The action locations form a schematic realized trajectory,
consistent with the other research illustrations. They do not simulate or
assert a particular allocation algorithm, optimization objective, or
target-finding rule. Only the conditional-law equation describes the design.

Two initial observations are followed by three new outcomes and the next
proposed assignment. Each observed outcome appears against the unchanged
old fit for 0.9 seconds before the curve and band update. The 26 frames last
14.2 seconds, including a 2.5-second final hold. The underlying outcome
function remains fixed; only its estimate and uncertainty change.

Colors match the policy-learning source: `blue!65` curve, `green!12` band,
`orange!55` next-experiment accent, and neutral black/gray axes and labels.
Measured points use `blue!65`; the latest measurement uses a `blue!80` dot
with a `blue!15` halo. Sans-serif labels and rounded line joins are shared.

The curve is generated by a toy Gaussian-process smoother with a
squared-exponential kernel (length scale 1.25, unit diagonal) and observation
noise SD `0.08`. The band's half-width is `1.2` posterior standard deviations.
This is a rendering device, not a prescribed estimator or a stated confidence
level. The illustrated observations lie on a fixed hidden mean function,
with zero realized noise. Interpolation between fitted models is only an
animation transition.

The figure introduces the adaptive observation model. It does not establish
valid inference, directional stability, or semiparametric efficiency; those
require the conditions and methods discussed in the accompanying research
text. Frame data are generated in the temporary build directory.

The research page plays the GIF automatically beneath the section introduction,
including when the detailed discussion is collapsed. Each illustration keeps
its natural aspect ratio. The static final slide is used when printing.


## Adversarial optimization

Edit `adversarial_optimization_frames.tex`, then run from the repository root:

```sh
python3 gifs/build_adversarial_optimization.py
```

Uses the same dependencies as the learning animation. It regenerates the
17-page frame PDF, animated GIF, and static final slide on a 1800-by-900 canvas.
The original mirror-descent and optimistic-mirror-descent coordinates and
iteration sequence are preserved. The comparison is schematic, rather than
an algorithm simulation or a quantitative saddle-level-set plot.

Typography, background, contours, trajectory colours, marker sizes, line
weights, and animation pauses follow the policy-learning illustration. The
numeric ticks and repeated overall title are omitted; sparse history markers
and a highlighted current point make each trajectory easier to follow.
