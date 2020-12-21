---
layout: page
title: Research
description: Jordy Van Landeghem's research
---

#### <u>Benchmarking Scalable Predictive Uncertainty in Text Classification.</u>
**Jordy Van Landeghem, Matthew Blaschko, Bertrand Anckaert and Marie-Francine Moens. To be submitted**
*This paper takes a position on the under-explored question of how predictive uncertainty methods perform in practice in Natural Language Processing, specifically multi-class and multi-label text classification. 
We conduct benchmarking experiments with 1-D convolutional neural networks and pre-trained transformers on six real-world text classification datasets in which we empirically investigate why popular scalable uncertainty estimation strategies (Monte-Carlo Dropout, Deep Ensemble) and notable extensions (Heteroscedastic, Concrete Dropout) underestimate uncertainty. We motivate complementary uncertainty estimation benefits from combining posterior approximation procedures, linking it to recent research on how ensembles and variational Bayesian methods navigate the loss landscape.
We find that our proposed method combination of Deep Ensemble with Concrete Dropout, by analysis of in-domain calibration, cross-domain classification, and novel class robustness, demonstrates superior performance, even at a smaller ensemble size. Our results corroborate the importance of fine-tuning dropout rate to the text classification task at hand, which individually and as an ensemble impacts model robustness. We observe in ablation that pretrained transformers severely underperform in novelty detection, limiting the applicability of transfer learning under the expectation of distribution shift from novel classes.*

[[PDF](), [BibTeX]()]

#### <u>Predictive Uncertainty for Probabilistic Novelty Detection in Text Classification.</u>
**Jordy Van Landeghem, Matthew Blaschko, Bertrand Anckaert and Marie-Francine Moens. ICML 2020 Workshop on Uncertainty and Robustness in Deep Learning**
*This paper experimentally reports on Bayesian predictive uncertainty for real-world text classification tasks. We compare Bayesian Deep Learning methods in text classification and define a straightforward protocol to evaluate the quality of uncertainty estimates. We report on Monte Carlo Dropout-based model and data uncertainties using 1-D convolutional neural networks on multi-class news topic and sentiment classification datasets. We find that our protocol effectively enables to test for novelty detection robustness showing that Bayesian quantities underestimate uncertainty and predictive entropy demonstrates superior performance.*

[[PDF]({{ BASE_PATH}}/pages/working_papers/UDL2020-paper-133.pdf), [slides]({{ BASE_PATH}}/pages/working_papers/UDL2020-slides-133.pdf),[BibTeX]({{ BASE_PATH}}/pages/working_papers/vanlandeghem2020a.bib)]

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->
