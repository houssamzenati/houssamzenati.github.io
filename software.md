---
layout: default
title: Software
permalink: /software/
---

<p class="software-intro">
I develop software for <strong>learning intervention rules</strong>, <strong>inferring</strong> intervention effects, and <strong>choosing actions as feedback arrives</strong>, alongside earlier implementations of generative models for anomaly detection.
</p>

## Open-source libraries:

<ul class="software-list software-list-library">
{% include software-card.html
  title="med_bench"
  venue="Psychological Methods"
  year="2025"
  url="https://judithabk6.github.io/med_bench/"
  image="med-bench"
  alt="Causal graph showing direct and mediated paths from treatment to outcome."
  description="A Python package for causal mediation analysis that implements the most common estimators within a unified framework, while allowing flexible choices for nuisance parameter models. It accompanies the paper <em>Causal mediation analysis with one or multiple mediators: a comparative study</em>."
%}
</ul>

## Open-source research software:

<ul class="software-list">
{% include software-card.html
  title="Interpretable distributional treatment effects"
  venue="NeurIPS"
  year="2026"
  url="https://github.com/houssamzenati/interpretable-dr-me-test"
  image="interpretable-dte"
  alt="Two experimental landscapes of the joint DR training criterion, each with a fixed first location v1 marked by an orange cross and a learned second location v2 marked by a blue star."
  description="Semiparametrically efficient local testing with learned outcome locations."
%}
{% include software-card.html
  title="adaptive-KTE"
  venue="AISTATS"
  year="2026"
  url="https://github.com/houssamzenati/adaptive-KTE"
  image="adaptive-kte"
  alt="Sequential observations and two outcome laws compared through the distance between their kernel mean embeddings."
  description="Kernel treatment effects with adaptively collected data."
%}
{% include software-card.html
  title="Counterfactual policy mean embeddings"
  venue="NeurIPS"
  year="2025"
  url="https://github.com/houssamzenati/counterfactual-policy-mean-embedding"
  image="cpme"
  alt="Two intervention outcome distributions mapped to distinct mean embeddings in a shared RKHS."
  description="Doubly robust estimation of counterfactual policy mean embeddings."
%}
{% include software-card.html
  title="Continuous-treatment mediation"
  venue="AISTATS"
  year="2025"
  url="https://github.com/houssamzenati/double-debiased-machine-learning-mediation-continuous-treatments"
  image="continuous-mediation"
  alt="Treatment and mediator pathways above a schematic dose-dependent mediated effect curve."
  description="Double debiased machine learning for mediation analysis with continuous treatments."
%}
{% include software-card.html
  title="Sequential counterfactual risk minimization"
  venue="ICML"
  year="2023"
  url="https://github.com/criteo-research/sequential-conterfactual-risk-minimization"
  image="sequential-crm"
  alt="Schematic sequential policy updates approach a risk minimum within an uncertainty band."
  description="Sequential counterfactual risk minimization for policy learning."
%}
{% include software-card.html
  title="Efficient Kernel UCB"
  venue="AISTATS"
  year="2022"
  url="https://github.com/criteo-research/Efficient-Kernel-UCB"
  image="kernel-ucb"
  alt="Kernel feature vectors projected onto a subspace spanned by selected dictionary features."
  description="Efficient kernelized UCB for contextual bandits."
%}
{% include software-card.html
  title="Nested bandits"
  venue="ICML"
  year="2022"
  url="https://github.com/criteo-research/Nested-Exponential-Weights"
  image="nested-bandits"
  alt="An action is selected through nested groups in an eight-leaf hierarchy."
  description="Nested exponential weights for nested bandits."
%}
{% include software-card.html
  title="Continuous-action counterfactual risk minimization"
  venue="ICLR Workshop on Causal Learning for Decision Making"
  year="2020"
  related_publication="TMLR · 2025"
  url="https://github.com/criteo-research/optimization-continuous-action-crm"
  image="continuous-crm"
  alt="A proximal surrogate guides an update of a continuous policy."
  description="Counterfactual learning and optimization of stochastic policies with continuous actions."
%}
{% include software-card.html
  title="Adversarially learned anomaly detection"
  venue="ICDM"
  year="2018"
  url="https://github.com/houssamzenati/Adversarially-Learned-Anomaly-Detection"
  image="alad"
  alt="ALAD encoder and generator with joint discrimination and cycle consistency."
  description="Adversarially learned models for anomaly detection."
%}
{% include software-card.html
  title="Efficient GAN anomaly detection"
  venue="ICLR Workshop (submitted)"
  year="2018"
  url="https://github.com/houssamzenati/Efficient-GAN-Anomaly-Detection"
  image="efficient-gan"
  alt="Efficient GAN generator and encoder with a joint discriminator."
  description="Efficient GAN-based anomaly detection."
%}
</ul>
