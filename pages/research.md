---
layout: page
title: Research
description: Jordy Van Landeghem's research
---

For more detail, check my Google Scholar profile: 
<a href="https://scholar.google.com/citations?user=Vsnb4d0AAAAJ&hl=en" align="left">
    <img src="{{ BASE_PATH }}/assets/gscholar.png" alt="Logo" width="50">
  </a>

### <u>Ph.D. Thesis: Intelligent Automation for AI-Driven Document Understanding </u>
**<u>Jury:</u> em. Prof. Dr. ir. Jean-Pierre Celis (chair), Prof. Dr. Marie-Francine Moens (supervisor), Prof. Dr. Matthew B. Blaschko (supervisor), Prof. Dr. ir. Johan Suykens, Prof. Dr. ir. Tinne Tuytelaars, Prof. Dr. Marcus Rohrbach (TU Darmstadt), Prof. Dr. Wenpeng Yin (Penn State University), Dr. Bertrand Anckaert (Contract.fit)**

*In a world where we are drowning in paperwork, from important legal documents to simple shopping bills, computers are stepping up to the challenge of helping us manage this endless stream of visually-rich documents. While our brains are wired to process visual information at lightning speeds, navigate a document's layout, and retrieve content effectively, artificial neural network-based models are still struggling to achieve the same level of understanding of complex, multimodal documents.
Despite the need for digitalization, organizations lag in adopting automated document processing solutions that can accurately handle these visually-rich documents. This gap in automation and accuracy poses a significant challenge for businesses and organizations that rely on efficient document processing to streamline their operations and improve productivity.*

*A major contribution of this thesis is the development of scalable and reliable methods for predicting uncertainty in natural language processing, a relatively uncharted area of research. The new method addresses concerns about robustness and control, which are crucial for businesses and organizations relying on accurate document processing. Another achievement of this work is a proposal to completely overhaul document classification methodology, bridging the gap between document understanding research and real-world applications. Furthermore, we introduce a comprehensive and versatile benchmark, DUDE, challenging the state-of-the-art in document understanding and fostering improvements across calibrated selective generation, and multimodal long-context processing. In sum, we promote more reliable, efficient, and realistic document processing, paving the way for greater adoption of these technologies in real-world applications.*

[[Manuscript]({{ BASE_PATH}}/assets/phdthesis/VanLandeghem_Jordy_PhD-thesis.pdf), [Slides-preliminary]({{ BASE_PATH}}/assets/phdthesis/VanLandeghemJordy_preliminary-defense.pdf), [Slides-public]({{ BASE_PATH}}/assets/phdthesis/VanLandeghemJordy_public-defense.pdf), [Code]({{ BASE_PATH}}/assets/phdthesis/thesis-code-and-data.md), [BibTeX]({{ BASE_PATH}}/assets/phdthesis/VanLandeghem2024phdthesis.bib)]

#### <u>Beyond Document Page Classification:Design, Datasets, Challenges </u>
**<u>Jordy Van Landeghem </u> (1,2)  Sanket Biswas (3), Matthew B. Blaschko (1), Marie-Francine Moens (1). (WACV 2024)**
( (1) KU Leuven, (2) Contract.fit, (3) CVC )

*This paper highlights the need to bring document classification benchmarking closer to real-world applications, both in the nature of data tested (X: multi-channel, multipaged, multi-industry; Y : class distributions and label set variety) and in classification tasks considered (f: multipage document, page stream, and document bundle classification, ...). We identify the lack of public multi-page document classification datasets, formalize different classification tasks arising in application scenarios, and motivate the value of targeting efficient multi-page document representations. 
An experimental study on proposed multi-page document classification datasets demonstrates that current benchmarks have become irrelevant and need to be updated to evaluate complete documents, as they naturally occur in practice. This reality check also calls for more mature evaluation methodologies, covering calibration evaluation, inference complexity (time-memory), and a range of realistic distribution shifts (e.g., born-digital vs. scanning noise, shifting page order). Our study ends on a hopeful note by recommending concrete avenues for future improvements.*

[[Link](https://openaccess.thecvf.com/content/WACV2024/papers/Van_Landeghem_Beyond_Document_Page_Classification_Design_Datasets_and_Challenges_WACV_2024_paper.pdf), [Slides]({{ BASE_PATH}}/assets/BDPC_WACV_1123.pdf), [Code](https://huggingface.co/bdpc/src)]

#### <u>Document UnderstanDing of Everything: DUDE😎, what’s next? (Seminar at Adobe Research).</u>
**<u>Jordy Van Landeghem </u> @09 October 2023

*In this talk, I will introduce the DUDE😎 project, a collaborative effort to foster research on generic document understanding. I will discuss the task paradigm of Document Visual Question-Answering (DocVQA) and the learning paradigm of Multi-Domain Long-Tailed Recognition (MDLT). Further, I will introduce how the DUDE dataset was created, why we set it up as an ICDAR 2023 competition, and elaborate on the proposed evaluation methodology. Finally, I will survey potential extensions solidifying DUDE’s role in further measurably advancing document understanding.*

[[Slides]({{ BASE_PATH}}/assets/231009_DUDE-whatsnext_JVL-Adobe.pdf)]

#### <u>Document Understanding Dataset and Evaluation (DUDE).</u>
**<u>Jordy Van Landeghem </u> (1,2), Łukasz Borchmann (3), Rubèn Tito (5), Michał Pietruszka (3,6), Dawid Jurkiewicz (3,7), Rafał Powalski (8),, Mickaël Coustaty (9), Bertrand Anckaert (2), Ernest Valveny (5), Matthew B. Blaschko (1), Marie-Francine Moens (1), Tomasz Stanisławek (3,4). (ICCV 2023)**
( (1) KU Leuven, (2) Contract.fit, (3) Snowflake, (4) Warsaw University of Technology, (5) CVC, (6) Jagiellonian University, (7) Adam Mickiewicz University, (8) Instabase, (9) University of La Rochelle)

*We call on the Document AI (DocAI) community to re-evaluate current methodologies and embrace the challenge of creating more practically-oriented benchmarks. Document Understanding Dataset and Evaluation (DUDE) seeks to remediate the halted research progress in understanding visually-rich documents (VRDs). We present a new dataset with novelties related to types of questions, answers, and document layouts based on multi-industry, multi-domain, and multi-page VRDs of various origins and dates. Moreover, we are pushing the boundaries of current methods by creating multi-task and multi-domain evaluation setups that more accurately simulate real-world situations where powerful generalization and adaptation under low-resource settings are desired. DUDE aims to set a new standard as a more practical, long-standing benchmark for the community, and we hope that it will lead to future extensions and contributions that address real-world challenges. Finally, our work illustrates the importance of finding more efficient ways to model language, images, and layout in DocAI.*

[[PDF](https://arxiv.org/abs/2305.08455), [BibTeX]({{ BASE_PATH}}/assets/VanLandeghem2023a.bib)]


#### <u>ICDAR 2023 Competition on Document UnderstanDing of Everything (DUDE).</u>
**<u>Jordy Van Landeghem </u> (1,2), Tomasz Stanisławek (3,4), Łukasz Borchmann (3), Rubèn Tito (5), Michał Pietruszka (3,6), Dawid Jurkiewicz (3,7), Rafał Powalski (8), Sanket Biswat (5), Mickaël Coustaty (9). (ICDAR 2023)**
( (1) KU Leuven, (2) Contract.fit, (3) Snowflake, (4) Warsaw University of Technology, (5) CVC, (6) Jagiellonian University, (7) Adam Mickiewicz University, (8) Instabase, (9) University of La Rochelle)

*We propose a new dataset for benchmarking Document Understanding systems under real-world settings that have been previously overlooked. In contrast to previous datasets, we extensively source multi-domain, 
multi-purpose, and multi-page documents of various types, origins, and dates. Importantly, we bridge the yet unaddressed gap between Document Layout Analysis and Question Answering paradigms by introducing complex layout-navigating questions and unique problems that often demand advanced information processing or multi-step reasoning. 
Finally, the multi-phased evaluation protocol also assesses the few-shot capabilities of models by testing their generalization power to previously unseen questions and domains, a condition essential to business use cases prevailing in the field.*


[[Competition](https://rrc.cvc.uab.es/?ch=23), [Code](https://github.com/duchallenge-team/dude/blob/main/README.md), [Slides]({{ BASE_PATH}}/assets/O11.4-slides.pdf), [Paper](https://doi.org/10.1007/978-3-031-41679-8_24)]

#### <u>Meeting Expectations: CVC Seminar.</u>
**<u>Jordy Van Landeghem </u> @30 June 2023

*While machine learning models are continually improving, for most tasks they fail to achieve perfect predictive performance. In order to be a valuable tool in decision-making under uncertainty, it stands to reason that we want some statistical guarantees on the quality of probabilistic predictive models. Research into calibration regained popularity after repeated empirical observations of overconfidence in Deep Neural Networks. This renewed interest sparked initiative relative to calibration metrics & remediation of miscalibration. This talk will focus on how to make use and sense of probabilistic predictions, with a primer on confidence estimation, calibration, and failure prediction. *

[[Link](https://www.cvc.uab.es/blog/2023/06/30/jordy-van-landeghem-cvc-seminar/), [Slides]({{ BASE_PATH}}/assets/230630_CVC-Seminar-JVL.pdf), [Code](https://github.com/Jordy-VL/calibration-primer)]



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
