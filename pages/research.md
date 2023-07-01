---
layout: page
title: Research
description: Jordy Van Landeghem's research
---

For more detail, check my Google Scholar profile: 
<a href="https://scholar.google.com/citations?user=Vsnb4d0AAAAJ&hl=en" align="left">
    <img src="{{ BASE_PATH }}/assets/gscholar.png" alt="Logo" width="50">
  </a>


#### <u>Meeting Expectations: CVC Seminar.</u>
**<u>Jordy Van Landeghem </u> 

*Meeting Expectations CVC Seminar @30 June 2023*

[[Link](https://www.cvc.uab.es/blog/2023/06/30/jordy-van-landeghem-cvc-seminar/), [Slides]({{ BASE_PATH}}/assets/233006_CVC-Seminar-JVL.pdf), [Code](https://github.com/Jordy-VL/calibration-primer)]

#### <u>ICDAR 2023 Competition on Document UnderstanDing of Everything (DUDE).</u>
**<u>Jordy Van Landeghem </u> (1,2), Tomasz Stanisławek (3,4), Łukasz Borchmann (3), Rubèn Tito (5), Michał Pietruszka (3,6), Dawid Jurkiewicz (3,7), Rafał Powalski (8), Sanket Biswat (5), Mickaël Coustaty (9). (ICDAR 2023)**
( (1) KU Leuven, (2) Contract.fit, (3) Snowflake, (4) Warsaw University of Technology, (5) CVC, (6) Jagiellonian University, (7) Adam Mickiewicz University, (8) Instabase, (9) University of La Rochelle)

*We propose a new dataset for benchmarking Document Understanding systems under real-world settings that have been previously overlooked. In contrast to previous datasets, we extensively source multi-domain, 
multi-purpose, and multi-page documents of various types, origins, and dates. Importantly, we bridge the yet unaddressed gap between Document Layout Analysis and Question Answering paradigms by introducing complex layout-navigating questions and unique problems that often demand advanced information processing or multi-step reasoning. 
Finally, the multi-phased evaluation protocol also assesses the few-shot capabilities of models by testing their generalization power to previously unseen questions and domains, a condition essential to business use cases prevailing in the field.*

[[Competition](https://rrc.cvc.uab.es/?ch=23), [Code](https://github.com/duchallenge-team/dude/blob/main/README.md)]

#### <u>Evaluating Strong Calibration for Probabilistic Structured Prediction.</u>
**Jordy Van Landeghem, Matthew Blaschko, and Marie-Francine Moens. (Unpublished)**

*While machine learning (ML) models are continually improving, for most tasks they fail to achieve perfect predictive performance. In order to be a valuable tool in decision-making under uncertainty, it stands to reason that we want some statistical guarantees on the quality of probability distribution outputs from probabilistic predictive models. Whereas research in statistics and ML has contributed different measures and tests for evaluating calibration, it has focused mainly on (i) classifiers predicting single discrete or real outputs, and (ii) miscalibration of only the most confident predictions (Niculescu-Mizil and Caruana, 2005; Naeini et al., 2015; Guo et al., 2017). 
However, many prototypical tasks in Natural Language Processing (NLP) involve sequential, structured output spaces (part-of-speech tagging, named entity recognition, machine translation, image captioning). While there exist increasingly stronger measures of calibration, ranging from top-1 and top-k to class-wise calibration, their usage in Structured Prediction (SP) is limited. We hypothesize this is due to the complexity associated with evaluating calibration over extremely high-dimensional, combinatorial output spaces. We argue that we are still in a position of finding feasible ways to estimate and bound calibration error for structured output spaces by taking into account the weighted and smoothed influence from unseen structures. We develop and motivate a general mathematical framework grounded in probability theory for valuating probabilistic structured predictors.*

#### <u>Benchmarking Scalable Predictive Uncertainty in Text Classification.</u>
**Jordy Van Landeghem, Matthew Blaschko, Bertrand Anckaert and Marie-Francine Moens.**

*This paper explores the question of how predictive uncertainty methods perform in practice in Natural Language Processing, specifically multi-class and multi-label text classification. We conduct benchmarking experiments with 1-D convolutional neural networks and pre-trained transformers on six real-world text classification datasets in which we empirically investigate why popular scalable uncertainty estimation strategies (Monte-Carlo Dropout, Deep Ensemble) and notable extensions (Heteroscedastic, Concrete Dropout) underestimate uncertainty. We motivate that uncertainty estimation benefits from combining posterior approximation procedures, linking it to recent research on how ensembles and variational Bayesian methods navigate the loss landscape. We find that our proposed method combination of Deep Ensemble with Concrete Dropout, by analysis of in-domain calibration, cross-domain classification, and novel class robustness, demonstrates superior performance, even at a smaller ensemble size. Our results corroborate the importance of fine-tuning dropout rate to the text classification task at hand, which individually and as an ensemble impacts model robustness. We observe in ablation that pre-trained transformers severely underperform in novelty detection, limiting the applicability of transfer learning when distribution shift from novel classes can be expected.*

[[PDF](https://ieeexplore.ieee.org/document/9761166), [BibTeX]({{ BASE_PATH}}/pages/working_papers/VanLandeghem2022IEEE.bib), [Code](https://github.com/Jordy-VL/uncertainty-bench)]

#### <u>Benchmarking Scalable Predictive Uncertainty in Text Classification.</u>
**Jordy Van Landeghem. Open Source Software**

*Perfect predictive accuracy is unattainable for most text classification problems, explaining the need for reliable ML solutions that can communicate predictive uncertainty when dealing with noisy or unknown inputs. In the quest for a simple, principled and scalable uncertainty method, which one to choose, when and why?
Our survey on Bayesian Deep Learning methods and benchmarking on 6 different text classification datasets aims to help practicioners make this decision and have future researchers spurred to continue investigations into hybrid uncertainty methods.
We open source our benchmark datasets, uncertainty method implementations, experimentation and evaluation setups (out-of-domain generalization, out-of-distribution robustness).*

[[BibTeX]({{ BASE_PATH}}/pages/working_papers/VanLandeghem2021_uncertaintybench.bib), [Code]({https://github.com/Jordy-VL/uncertainty-bench})]


#### <u>Predictive Uncertainty for Probabilistic Novelty Detection in Text Classification.</u>
**Jordy Van Landeghem, Matthew Blaschko, Bertrand Anckaert and Marie-Francine Moens. ICML 2020 Workshop on Uncertainty and Robustness in Deep Learning**

*This paper experimentally reports on Bayesian predictive uncertainty for real-world text classification tasks. We compare Bayesian Deep Learning methods in text classification and define a straightforward protocol to evaluate the quality of uncertainty estimates. We report on Monte Carlo Dropout-based model and data uncertainties using 1-D convolutional neural networks on multi-class news topic and sentiment classification datasets. We find that our protocol effectively enables to test for novelty detection robustness showing that Bayesian quantities underestimate uncertainty and predictive entropy demonstrates superior performance.*

[[PDF]({{ BASE_PATH}}/pages/working_papers/UDL2020-paper-133.pdf), [slides]({{ BASE_PATH}}/pages/working_papers/UDL2020-slides-133.pdf),[BibTeX]({{ BASE_PATH}}/pages/working_papers/Vanlandeghem2020a.bib)]

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->
