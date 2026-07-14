---
layout: default
title: "Nuisance-Robust Learning and Inference"
permalink: /research/
hide_title: true
---

<div class="research-identity">
  <h1 class="research-identity-title">Nuisance-Robust Learning and&nbsp;Inference</h1>
  <p class="research-identity-subtitle">Methods for imperfect, adaptive and structured feedback</p>
</div>

<p class="research-overview">
Modern machine learning increasingly relies on pipelines in which learned models guide decisions, decisions determine which data are observed, and those data are reused for inference and further optimization. The same mechanisms that make these systems effective&mdash;adaptive collection, flexible prediction, learned representations, and optimization through estimated components&mdash;can invalidate classical guarantees. Component-wise guarantees need not survive composition: deployment changes the sampling law, optimization amplifies estimation error, and plug-in procedures propagate bias downstream.
</p>

<figure class="research-overview-gif">
  <img src="{{ "/gifs/composition_guarantees.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated pipeline showing learned models, decisions, observed data, inference, failure mechanisms, and repair principles">
</figure>

<p class="research-overview">
My research develops statistical theory and algorithms for these interfaces. I study where guarantees fail when learning, optimization, and inference interact; identify conditions and constructions&mdash;such as directional stability and orthogonality&mdash;that preserve validity and efficiency; and design principled corrections when they do not. The broader goal is to enable expressive learning systems to improve decisions without compromising the conclusions drawn from them. This programme spans inference after adaptive experiments, nuisance-robust distributional causal inference for structured outcomes, nuisance-robust methods for functionals of solutions of inverse and nested problems, policy learning, and earlier work in representation learning.
</p>

<details class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Statistical Foundations of Inference after Adaptive Experiments</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>

    <figure class="research-gif">
      <img src="{{ "/gifs/adaptive_inference.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated adaptive experiment, orthogonal score, and Gaussian inference pipeline">
    </figure>
  </summary>

  <div class="research-block-content">
    <p>
      Adaptive experiments use past outcomes to choose future assignments, then reuse the resulting trajectory for inference. For estimators whose leading term is a martingale sum, a Gaussian limit typically requires two ingredients: no individual increment is asymptotically influential, and the normalized quadratic variation&mdash;or, under mild conditions, the accumulated conditional variance&mdash;stabilizes. Adaptive allocation can violate the second requirement because the realized assignment path may preserve non-negligible information about earlier outcome fluctuations; in fixed-horizon examples, an inverse-propensity estimator with known assignment probabilities then converges to a non-Gaussian mixture of normals. It can also violate the first requirement when some assignment probabilities are of order $1/T$, allowing a few inverse-propensity-weighted observations to retain non-vanishing influence. Consequently, naive Wald intervals based on the standard martingale Gaussian approximation can be miscalibrated.
    </p>

    <p>
      I develop procedures that restore validity while preserving the information accumulated by the adaptive design. For structured outcomes, I construct a learn-then-test procedure that estimates an informative witness direction, projects a doubly robust RKHS score onto it, and applies predictable variance normalization, yielding calibrated distributional tests under adaptive assignment <a href="https://arxiv.org/pdf/2510.10245">[AI1]</a>. In my recent work, I introduce directional stability, a target-specific condition requiring only the design information relevant to the parameter of interest&mdash;formalized through its Riesz representer&mdash;to stabilize, rather than the entire information matrix. To characterize efficiency in this setting, I develop local asymptotic normality and convolution theory for sequences of experiments whose adaptive sampling laws change with the horizon. Within this theory, I show that directional stability is sufficient for classical one-step estimators to remain asymptotically normal and attain the semiparametric efficiency bound, without generic adaptive reweighting <a href="https://arxiv.org/abs/2602.21478">[AI2]</a>.
    </p>

    <p>
      Questions:
    </p>

    <div class="research-questions">
      <p>
        How can distributional tests remain calibrated when adaptive assignment changes the covariance geometry of the outcome representation? <a href="https://arxiv.org/pdf/2510.10245">[AI1]</a>
      </p>

      <p>
        What target-specific stability is sufficient for classical one-step inference to remain valid and efficient under adaptive sampling? <a href="https://arxiv.org/abs/2602.21478">[AI2]</a>
      </p>

      <p>
        How should semiparametric efficiency be defined when the sampling law itself changes with the experiment? <a href="https://arxiv.org/abs/2602.21478">[AI2]</a>
      </p>
    </div>

  </div>
</details>

<details class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Distributional Causal Inference for Structured Outcomes</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>

    <figure class="research-gif">
      <img src="{{ "/gifs/mean_embedding.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated kernel mean embedding comparison for interventional outcome distributions">
    </figure>
  </summary>

  <div class="research-block-content">
    <p>
      Most causal inference reduces intervention effects to means, quantiles, or other scalar summaries. This can miss changes in dispersion, modes, tails, or rare configurations, while the field still lacks a general statistical theory and broadly applicable machine-learning methods for causal inference with images, sequences, graphs, and other structured outcomes. I address this gap by developing kernel-based procedures that represent entire interventional outcome distributions while remaining robust to estimation errors in propensity and conditional outcome models.
    </p>

    <p>
      I first introduced a global, doubly robust representation and test for determining whether two interventions induce the same outcome distribution <a href="https://arxiv.org/pdf/2506.02793">[SO1]</a>. An omnibus rejection, however, establishes that the distributions differ without revealing how. I therefore developed a second procedure that learns informative outcome prototypes and evaluates the discrepancy at those locations, yielding an interpretable and semiparametrically efficient test that localizes the effect while remaining valid after data-driven prototype selection <a href="https://arxiv.org/pdf/2605.08034">[SO2]</a>.
    </p>

    <div class="research-questions">
      <p>
        How can entire interventional outcome distributions be represented, estimated, and compared for structured outcomes? <a href="https://arxiv.org/pdf/2506.02793">[SO1]</a>
      </p>

      <p>
        How can a global distributional difference be localized and interpreted without sacrificing statistical efficiency or validity after data-driven selection? <a href="https://arxiv.org/pdf/2605.08034">[SO2]</a>
      </p>
    </div>

  </div>
</details>

<details class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Nuisance-Robust Learning and Inference for Nested and Inverse Problems</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>

    <figure class="research-gif">
      <img src="{{ "/gifs/newton_geometry.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated local Newton geometry for nuisance-robust nested and inverse problems">
    </figure>
  </summary>

  <div class="research-block-content">
    <p>
      I develop nuisance-robust methods for finite-dimensional functionals of solutions to nested and inverse problems. In mediation and bilevel optimization, these functionals are built from iterated regressions or a lower-level population optimizer and its derivative; in proxy and instrumental-variable analysis, they are built from bridge or least-squares solutions to conditional moment equations. Plug-in estimation is fragile: errors propagate through nested layers, while inverse operators discard information, making exact solutions unstable, non-unique, or potentially nonexistent. I therefore target the final functional directly using orthogonal scores, Riesz corrections, complementary bridge equations, and cross-fitting.
    </p>

    <p>
      For mediation, I developed a kernel-localized orthogonal estimator for continuous-treatment mediated response curves <a href="https://arxiv.org/abs/2503.06156">[N1]</a>. A companion comparative mediation study benchmarks classical, multiply robust, and double-machine-learning estimators across binary, continuous, and multidimensional mediators, including under model misspecification, weak overlap, and in a UK Biobank application <a href="https://arxiv.org/pdf/2505.07323">[N2]</a>. For latent confounding, in joint work we developed density-ratio-free doubly robust bridge estimators based on kernel mean embeddings <a href="https://arxiv.org/pdf/2505.19807">[N3]</a>. In more recent joint work on instrumental variables, we introduced a projected parameter defined through primal and dual population least-squares problems. It remains well defined when the exact moment equations have no solution, is invariant to non-unique least-squares minimizers, and coincides with the usual structural estimand under exact specification <a href="https://arxiv.org/pdf/2604.24660">[N4]</a>. We subsequently extended the bridge approach to neural representations and continuous or structured treatments <a href="https://arxiv.org/pdf/2605.09514">[N5]</a>. I also developed the first semiparametric efficiency theory for the unregularized population bilevel gradient, together with an orthogonal estimator controlled uniformly over the outer parameter so that it can serve as a statistical gradient oracle <a href="https://arxiv.org/abs/2605.21341">[N6]</a>.
    </p>

    <p>
      <strong>Recent questions</strong>
    </p>

    <div class="research-questions">
      <p>
        What should nonparametric IV analysis estimate when its moment equations are only approximate? Can a projected least-squares parameter recover the usual estimand under exact specification and still support debiased inference otherwise? <a href="https://arxiv.org/pdf/2604.24660">[N4]</a>
      </p>

      <p>
        How can the unregularized population hypergradient be estimated without the first-order bias of differentiating fitted lower-level models, and controlled uniformly enough to guide optimization? <a href="https://arxiv.org/abs/2605.21341">[N6]</a>
      </p>
    </div>

    <h3>Selected Papers</h3>

    <ul class="selected-papers">
      <li>
        <strong>[N4] Nonparametric Instrumental Variable Analysis Without Structural Equations: Debiased Inference on Functionals of Inverse Problems with No Solutions</strong><br>
        Zikai Shen, Nathan Kallus, Dimitri Meunier, <strong><em>Houssam Zenati</em></strong>, Arthur Gretton, Aur&eacute;lien Bibaut.<br>
        <em>Preprint</em>, 2026.<br>
        <a href="https://arxiv.org/pdf/2604.24660">[Paper]</a>
      </li>
      <li>
        <strong>[N6] Semiparametric Efficient Bilevel Gradient Estimation</strong><br>
        Fares El Khoury*, <strong><em>Houssam Zenati</em></strong>*, Nathan Kallus, Michael Arbel, Aurelien Bibaut.<br>
        <em>Preprint</em>, 2026.<br>
        <a href="https://arxiv.org/abs/2605.21341">[Paper]</a>
      </li>
    </ul>
  </div>
</details>

<details class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Statistical and Algorithmic Foundations of Policy Learning</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>

    <figure class="research-gif">
      <img src="{{ "/gifs/policy_learning.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated policy-learning trajectory and deployment loop">
    </figure>
  </summary>

  <div class="research-block-content">
    <p>
      I develop statistical and algorithmic foundations for policy learning across fully online, batched-online, and offline contextual-bandit settings. In online contextual bandits, I study both value-based methods, which model conditional rewards, and policy-based methods, which compete directly with the best policy in a class without reward-model realizability. I made nonparametric kernel value-based learning computationally scalable through incremental Nystr&ouml;m approximations <a href="https://proceedings.mlr.press/v151/zenati22a.html">[PL2]</a>. On the policy-based side, I introduced in Sequential CRM a H&ouml;lderian error-bound principle linking policy suboptimality to importance-weight variance. Combined with variance-sensitive updates and limited redeployment, this yields fast excess-risk and regret rates for parametric policy classes <a href="https://arxiv.org/pdf/2302.12120.pdf">[PL4]</a>. I then extended this principle to fully online, agnostic learning over rich nonparametric classes: O2PL establishes the first fast best-in-class regret rates, including nonparametric classes <a href="https://arxiv.org/abs/2510.15483">[PL7]</a>.
    </p>

    <p>
      From fixed logged data, I developed methods for learning stochastic policies with continuous actions. I first addressed the resulting nonconvex optimization problem through smooth importance weighting and proximal methods <a href="https://causalrlworkshop.github.io/program/cldm_6.html">[PL1]</a>, then completed the pipeline with joint context&ndash;action kernel models and principled offline model selection and evaluation <a href="https://arxiv.org/pdf/2004.11722.pdf">[PL6]</a>. My recent work introduces a semiparametric natural-gradient construction that debiases the learned policy itself, rather than merely estimating or optimizing a debiased policy value <a href="https://arxiv.org/pdf/2603.28681">[PL8]</a>.
    </p>

    <p>
      Complementing this contextual-bandit programme, I studied how structure in the decision space can reduce the effective complexity of online exploration: through hierarchical similarities between actions <a href="https://proceedings.mlr.press/v162/martin22a/martin22a.pdf">[PL3]</a> and covariance information revealed by semi-bandit observations <a href="https://arxiv.org/pdf/2402.15171">[PL5]</a>. Building on these foundations, my recent work asks:
    </p>

    <div class="research-questions">
      <p>
        What structural conditions allow fully online, agnostic contextual bandits to attain fast regret against the best policy in a rich nonparametric class, without reward-model realizability? <a href="https://arxiv.org/abs/2510.15483">[PL7]</a>
      </p>

      <p>
        Can policy learning itself, not merely the evaluation of a fixed policy, be semiparametrically targeted through a functional natural-gradient flow, so that rich policy classes attain root-N regret while policy approximation and environment-estimation errors interact only through second-order product remainders? <a href="https://arxiv.org/pdf/2603.28681">[PL8]</a>
      </p>
    </div>

    <h3>Selected Papers</h3>

    <ul class="selected-papers">
      <li>
        <strong>[PL4] Sequential Counterfactual Risk Minimization</strong><br>
        <strong><em>Houssam Zenati</em></strong>, Eustache Diemert, Matthieu Martin, Julien Mairal, Pierre Gaillard.<br>
        <em>ICML</em>, 2023.<br>
        <a href="https://arxiv.org/pdf/2302.12120.pdf">[Paper]</a> &middot; <a href="https://github.com/criteo-research/sequential-counterfactual-risk-minimization">[Code]</a>
      </li>
      <li>
        <strong>[PL7] Fast Best-in-Class Regret for Contextual Bandits</strong><br>
        Samuel Girard, Aurelien Bibaut, Arthur Gretton, Nathan Kallus, <strong><em>Houssam Zenati</em></strong>.<br>
        <em>UAI</em>, 2026.<br>
        <a href="https://arxiv.org/abs/2510.15483">[Paper]</a>
      </li>
      <li>
        <strong>[PL8] Functional Natural Policy Gradients</strong><br>
        Aurelien Bibaut, <strong><em>Houssam Zenati</em></strong>, Thibaud Rahier, Nathan Kallus.<br>
        <em>Preprint</em>, 2026.<br>
        <a href="https://arxiv.org/pdf/2603.28681">[Paper]</a>
      </li>
    </ul>
  </div>
</details>

<details class="research-block research-collapsible">
  <summary class="research-block-summary">
    <div class="research-block-header">
      <h2>Generative Representation Learning and Adversarial Optimization</h2>
      <span class="research-toggle" aria-hidden="true"></span>
    </div>

    <figure class="research-gif">
      <img src="{{ "/gifs/adversarial_optimization.gif" | relative_url }}?v={{ site.time | date: "%s" }}" alt="Animated optimization dynamics for adversarial learning, comparing mirror descent and optimistic mirror descent">
    </figure>
  </summary>

  <div class="research-block-content">
    <p>
      My earlier work in adversarial learning first focused on generative representation learning for anomaly detection and semi-supervised prediction. I initiated and led a line of work that made GAN-based anomaly detection practical at test time. I introduced an amortized detector that replaced the costly per-example latent optimization used by earlier GAN methods with direct encoder-based inference, achieving state-of-the-art results while reducing test-time computation by several hundred-fold <a href="https://arxiv.org/pdf/1802.06222.pdf">[AR1]</a>. I then developed ALAD, strengthening bidirectional adversarial learning with data- and latent-space cycle consistency, spectral normalization, and discriminator-based representations to improve anomaly detection across image and tabular benchmarks <a href="https://arxiv.org/pdf/1812.02288.pdf">[AR4]</a>. This line of work became a widely cited reference point in generative anomaly detection, and ALAD was subsequently used beyond the original benchmarks.
    </p>

    <p>
      I also contributed to work showing how GANs can encode data-manifold geometry through a Monte Carlo approximation of Laplacian regularization for semi-supervised learning <a href="https://arxiv.org/pdf/1805.08957.pdf">[AR2]</a>, <a href="https://arxiv.org/abs/1807.04307">[AR3]</a>, and to studies using semi-supervised and unsupervised representation learning to reduce reliance on expert annotations in retinal imaging <a href="https://arxiv.org/pdf/1812.07832.pdf">[AR5]</a>, <a href="https://link.springer.com/chapter/10.1007/978-3-030-33391-1_26">[AR7]</a>.
    </p>

    <p>
      A complementary line of work examined optimization in adversarial min&ndash;max problems. It characterized the last-iterate dynamics of mirror descent under coherence, showed why standard updates can cycle even in bilinear games, and established convergence of optimistic corrections across the broader class of coherent problems <a href="https://openreview.net/pdf?id=Bkg8jjC9KQ">[AR6]</a>.
    </p>

    <p>
      Questions:
    </p>

    <div class="research-questions">
      <p>
        How can adversarial generative models make anomaly detection both accurate and computationally practical, avoiding per-example latent optimization at inference time? <a href="https://arxiv.org/pdf/1802.06222.pdf">[AR1]</a>, <a href="https://arxiv.org/pdf/1812.02288.pdf">[AR4]</a>
      </p>

      <p>
        How can generators encode data-manifold geometry and exploit unlabeled observations for semi-supervised learning? <a href="https://arxiv.org/pdf/1805.08957.pdf">[AR2]</a>, <a href="https://arxiv.org/abs/1807.04307">[AR3]</a>
      </p>

      <p>
        How can representation learning reduce expert-annotation requirements in medical imaging? <a href="https://arxiv.org/pdf/1812.07832.pdf">[AR5]</a>, <a href="https://link.springer.com/chapter/10.1007/978-3-030-33391-1_26">[AR7]</a>
      </p>

      <p>
        Under what structural conditions do optimistic first-order methods achieve last-iterate convergence in adversarial min&ndash;max problems? <a href="https://openreview.net/pdf?id=Bkg8jjC9KQ">[AR6]</a>
      </p>
    </div>

    <h3>Selected Papers</h3>

    <ul class="selected-papers">
      <li>
        <strong>[AR1] Efficient GAN-Based Anomaly Detection</strong><br>
        <strong><em>Houssam Zenati</em></strong>, Chuan-Sheng Foo, Bruno Lecouat, Gaurav Manek, Vijay Ramaseshan Chandrasekhar.<br>
        <em>ICLR Workshop</em>, 2018.<br>
        <a href="https://arxiv.org/pdf/1802.06222.pdf">[Paper]</a> &middot; <a href="https://github.com/houssamzenati/Efficient-GAN-Anomaly-Detection">[Code]</a>
      </li>
      <li>
        <strong>[AR4] Adversarially Learned Anomaly Detection</strong><br>
        <strong><em>Houssam Zenati</em></strong>, Manon Romain, Chuan-Sheng Foo, Bruno Lecouat, Vijay Chandrasekhar.<br>
        <em>ICDM</em>, 2018.<br>
        <a href="https://arxiv.org/pdf/1812.02288.pdf">[Paper]</a> &middot; <a href="https://github.com/houssamzenati/Adversarially-Learned-Anomaly-Detection">[Code]</a>
      </li>
      <li>
        <strong>[AR6] Optimistic Mirror Descent in Saddle-Point Problems: Going the Extra (Gradient) Mile</strong><br>
        Panagiotis Mertikopoulos, Bruno Lecouat, <strong><em>Houssam Zenati</em></strong>, Chuan-Sheng Foo, Vijay Chandrasekhar, Georgios Piliouras.<br>
        <em>ICLR</em>, 2019.<br>
        <a href="https://openreview.net/pdf?id=Bkg8jjC9KQ">[Paper]</a> &middot; <a href="https://github.com/bruno-31/gan_optim">[Code]</a>
      </li>
    </ul>
  </div>
</details>
