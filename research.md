---
layout: default
title: "Statistical Learning for Inference and Decision-Making"
permalink: /research/
hide_title: true
math: true
---

<div class="research-identity">
  <h1 class="research-identity-title">Statistical Learning for Inference and Decision-Making</h1>
</div>

<p class="research-overview">
The evidence needed to improve a decision rule can differ from the evidence needed to quantify its effects. My research examines how risk geometry, the structure of inferential targets, and experimental design determine what can be learned from limited feedback. Across these problems, I seek guarantees that reflect <strong>the accuracy and information required by the final task</strong>.
</p>

<details id="learning-to-intervene" class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Learning to Intervene</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>
    <p class="research-block-intro">
      Learning to intervene means using selective feedback from past actions to <strong>improve an intervention rule</strong> \(\pi\). I study how much feedback is needed to approach the performance of the best rule \(\pi^\star\) in a chosen class \(\Pi\), and how much regret accumulates during sequential learning.
    </p>
    {% include research-figure.html
      name="policy_learning"
      title="Learning to intervene"
      width="1800"
      height="901"
      alt="A policy pi improves from pi-zero toward the best-in-class rule pi-star within the class Pi. Orange contours show illustrative risk levels. Logged actions and outcomes support learning; a dashed deployment loop adds new feedback in the sequential setting."
      caption="Starting from \(\pi_0\), the illustration follows an improving policy through risk contours. The path can represent continuous improvement or successive updates; the dashed loop adds feedback from deployment."
    %}
  </summary>

  <div class="research-block-content">
    <p>For an expected loss \(R(\pi)\), the best-in-class objective is</p>
    <div class="research-equation">
      \[
        \pi^\star\in\operatorname*{arg\,min}_{\pi\in\Pi}R(\pi).
      \]
    </div>
    <p>Learning reduces the <em>excess risk</em> \(R(\pi)-R(\pi^\star)\).</p>

    <h3>What determines how quickly we can approach the best policy in a chosen class?</h3>
    <p>
      My <a href="https://arxiv.org/abs/2004.11722">continuous-action CRM work</a> develops representations, optimization methods and evaluation procedures for learning stochastic policies from logged feedback. The statistical difficulty depends in part on how differences in policy performance compare with the uncertainty in estimating them.
    </p>
    <p>
      In <a href="https://arxiv.org/abs/2302.12120">Sequential CRM</a>, I identify geometric conditions linking policy suboptimality to importance-weight variance. Algorithms can exploit this relationship to achieve faster learning: <strong>fewer observations for a given policy performance, or less regret during deployment</strong>. <a href="https://arxiv.org/abs/2510.15483">O2PL</a> develops this fast-rate principle for rich policy classes under fully online updating, without assuming that a reward model is correctly specified.
    </p>

    <h3>Can structure in the environment reduce the statistical cost of learning a rich policy class?</h3>
    <p>
      Risk geometry is one source of favorable learning rates. Another is the interaction between policy-class complexity and how accurately the environment can be learned. In <a href="https://arxiv.org/abs/2603.28681">Functional Natural Policy Gradients</a>, we construct a correction of the learned policy through a cross-fitted natural-gradient flow. The resulting guarantees <strong>couple policy and environment-estimation errors</strong>, allowing sufficiently learnable environmental structure to compensate for a rich policy class.
    </p>
    <p>
      An ongoing question connects learning to inference: <em>how can we learn policies whose improvement over a reference rule can also be statistically established?</em>
    </p>
  </div>
</details>

<details id="inference-on-intervention-effects" class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Inference on Intervention Effects</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>
    <p class="research-block-intro">
      Learning which interventions perform well leaves further questions about <strong>what they change and how precisely their effects can be established</strong>. I study distributional effects and targets defined through nested or inverse problems, including mediated effects and inference under unobserved confounding.
    </p>
    {% include research-figure.html
      name="nuisance_robust_inference"
      title="Inference on intervention effects"
      width="1800"
      height="600"
      alt="Nearby nuisance estimates eta-hat, such as outcome or treatment models, vary in blue while the data remain fixed. Orthogonal bias correction maps them to corrected estimates theta-hat with reduced local sensitivity. The red star marks the true target, distinct from the estimate."
      caption="With the observations held fixed, nearby nuisance fits \(\widehat\eta\) produce corrected estimates \(\widehat\theta\) with reduced local sensitivity. Sampling uncertainty remains."
    %}
  </summary>

  <div class="research-block-content">
    <p>
      Effect estimators often incorporate functions learned through prediction tasks, such as outcome or treatment-assignment models. In the illustration, these fitted functions are denoted by \(\widehat\eta\), and the final target estimate by \(\widehat\theta\). <strong>Good prediction does not guarantee good decisions or valid inference—and good decisions and valid inference do not always require highly accurate predictions.</strong> I characterize which estimation errors affect the target and develop corrections that reduce their influence.
    </p>

    <h3>What changes beyond the mean, and how can those changes be understood?</h3>
    <p>
      Interventions can have similar average outcomes while changing variability, tails or other features of the outcome distribution. My <a href="https://arxiv.org/abs/2506.02793">counterfactual policy mean-embedding work</a> represents and compares interventional outcome distributions, including for structured outcomes such as images and sequences.
    </p>
    <p>
      A global test can establish that distributions differ without explaining which features distinguish them. My <a href="https://arxiv.org/abs/2605.08034">interpretable distributional test</a> learns informative outcome locations and evaluates discrepancies there, while accounting for their data-driven selection. A complementary ongoing direction develops scalable sampling from estimated interventional distributions, making those distributions easier to explore through representative outcomes.
    </p>

    <h3>How can we infer functionals defined through nested regressions or inverse equations?</h3>
    <p>
      <strong>In nested problems, estimation errors propagate across layers.</strong> Mediated effects depend on nested conditional expectations; my <a href="https://arxiv.org/abs/2503.06156">continuous-treatment mediation work</a> develops corrected estimation and uncertainty quantification for mediated-response curves. These questions also motivate longitudinal extensions, where later decisions and outcomes depend on evolving histories. A related problem arises in optimization: my <a href="https://arxiv.org/abs/2605.21341">bilevel-gradient work</a> corrects the bias introduced when a population gradient depends on a learned lower-level optimizer.
    </p>
    <p>
      <strong>In inverse problems, recovering an entire function can be unstable or ambiguous.</strong> Proxies and instrumental variables provide indirect information about effects under unobserved confounding. The relevant question is whether a particular functional can be estimated accurately even when the bridge or structural function is difficult to recover. Our proxy work develops <a href="https://arxiv.org/abs/2505.19807">kernel</a> and <a href="https://arxiv.org/abs/2605.09514">neural</a> estimators that combine complementary bridge functions and control the errors relevant to the final target.
    </p>
    <p>
      <strong>What should inference target when the inverse equations have no exact solution?</strong> Our <a href="https://arxiv.org/abs/2604.24660">NPIV preprint</a> addresses this further difficulty through a projected functional. It remains well defined without an exact solution and recovers the conventional estimand under exact specification.
    </p>
  </div>
</details>

<details id="adaptive-experimentation" class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Adaptive Experimentation</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>
    <p class="research-block-intro">
      Learning and inference meet in deciding what to try next. <strong>The interventions that appear best for performance need not be those that are most informative about the effects we want to estimate.</strong> Adaptive experimentation asks how to pursue both aims as outcomes arrive and guide subsequent choices. Each choice affects the outcomes we obtain and the evidence on which later decisions and conclusions depend. I develop exploration algorithms that exploit structure, establish conditions for valid and efficient inference as assignments adapt, and investigate how inferential goals should guide further experimentation.
    </p>
    {% include research-figure.html
      name="adaptive_inference"
      title="Adaptive experimentation"
      width="1800"
      height="700"
      alt="An adaptive experiment with assigned actions on the horizontal axis and observed outcomes on the vertical axis. The observation law separates history-dependent assignment from a fixed outcome law. An orange ring marks the next assignment; new outcomes update the blue estimated mean and green model uncertainty."
      caption="New observations update the estimated mean outcome \(\widehat m_t(a)\). Orange marks the next assignment; green illustrates uncertainty in the fitted model."
    %}
  </summary>

  <div class="research-block-content">
    <p>With context held fixed, the observation model in the illustration is</p>
    <div class="research-equation">
      \[
        p_{t+1}(a,y\mid\mathcal H_t)
        =
        g_{t+1}(a\mid\mathcal H_t)\,q_0(y\mid a).
      \]
    </div>
    <p>
      The assignment rule \(g_{t+1}\) depends on the observed history \(\mathcal H_t\), while the conditional outcome law \(q_0\) stays fixed. <strong>Changing assignments therefore changes where information accumulates</strong>, even though the underlying outcome mechanism remains the same.
    </p>

    <h3>How can structure reduce the cost of exploration?</h3>
    <p>
      My work exploits complementary forms of structure: <a href="https://proceedings.mlr.press/v151/zenati22a.html">kernel approximations</a> make contextual exploration computationally scalable, <a href="https://proceedings.mlr.press/v162/martin22a.html">nested action similarities</a> allow information to be shared across related actions, and <a href="https://arxiv.org/abs/2402.15171">covariance information</a> improves learning from semi-bandit feedback.
    </p>

    <h3>What can we conclude from data collected by an adaptive decision rule?</h3>
    <p>
      Concentrating observations on promising actions can reduce information about alternative interventions. Dependence on earlier outcomes can also invalidate familiar inferential procedures, even when assignment probabilities are known.
    </p>
    <p>
      I study two complementary responses. <a href="https://arxiv.org/abs/2510.10245">Adaptive kernel treatment effects</a> combine learned witness directions with sequential normalization to obtain calibrated distributional tests. <a href="https://arxiv.org/abs/2602.21478">Directional stability</a> identifies conditions under which <strong>the information relevant to a scalar target stabilizes</strong> sufficiently for classical one-step estimators to remain valid and efficient, without requiring the entire design to stabilize.
    </p>

    <h3>How much exploration does a particular inferential target require?</h3>
    <p>
      An ongoing question is how to connect inferential precision to the assignments needed to obtain it: <em>which experiments improve estimation of a specified effect, and what do they cost in policy performance?</em> This brings the learning and inference questions back into the design of data collection.
    </p>
  </div>
</details>

<details id="adversarial-optimization" class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Generative Models and Representation Learning</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>
    <p class="research-block-intro">
      My work on generative models studies how <strong>learned representations support anomaly detection and prediction with limited labels</strong>, alongside the optimization dynamics used to train adversarial models.
    </p>
    {% include research-figure.html
      name="adversarial_optimization"
      title="Adversarial optimization"
      width="1800"
      height="900"
      alt="Mirror descent and optimistic mirror descent start at the same x-zero. Blue trajectories show the first method spiraling outward while optimistic corrections keep the updates near the red equilibrium x-star."
      caption="Two illustrative trajectories begin at the same \(x_0\). Optimistic corrections alter the dynamics around the equilibrium \(x^\star\)."
    %}
  </summary>

  <div class="research-block-content">
    <h3>How can generative representations make learning with limited labels practical?</h3>
    <p>
      My <a href="https://arxiv.org/abs/1802.06222">encoder-based anomaly detection</a> and <a href="https://arxiv.org/abs/1812.02288">ALAD</a> work replaces costly per-example latent optimization with direct inference and develops representations for detecting anomalies in image and tabular data. Related work uses <a href="https://arxiv.org/abs/1805.08957">generative models to capture data-manifold geometry</a>, allowing unlabeled observations to support semi-supervised prediction.
    </p>

    <h3>Under what conditions can adversarial optimization be stabilized?</h3>
    <p>
      Adversarial training couples interacting optimization variables, represented by \(x=(x_1,x_2)\) in the illustration. Standard updates can cycle around an equilibrium \(x^\star\). Our work on <a href="https://openreview.net/forum?id=Bkg8jjC9KQ">optimistic mirror descent</a> characterizes these dynamics and establishes convergence under coherence and suitable step-size conditions.
    </p>
  </div>
</details>

<p class="document-links"><a href="{{ '/publications/' | relative_url }}">All publications</a></p>

<script src="{{ '/assets/js/research.js' | relative_url }}" defer></script>
