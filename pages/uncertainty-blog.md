---
layout: page
title: Uncertainty in Deep Learning
description: Jordy Van Landeghem's research
---



Uncertainty Methods
===================

First, we formally present in Subsection [1](#section:background) how uncertainty is quantified in Deep Learning with an introduction to Bayesian modeling.
Subsection [2](#section:preduquant) treats predictive uncertainty methods with a focus on the algorithmic procedure, followed by representative method extensions for more reliable uncertainty estimation. Subsection [3](#section:uquant) is devoted to uncertainty estimation: from what sources uncertainty originates, how to categorize different uncertainty measures, and how to quantify uncertainty at test-time with the methods from the previous Subsection.


Quantifying Uncertainty in Deep Learning {#section:background}
----------------------------------------

In modern Deep Learning, two common uncertainty (or inversely
"confidence\") estimates are the prediction probability over classes,
known as *softmax-score*, and the *predictive entropy* over posterior
class probabilities [@Shannon48; @Zaragoza1998ConfidenceMF]. However,
@guo2017calibration's work on confidence calibration demonstrated these
to be unreliable estimates of Neural Networks' uncertainty.\
**Bayesian Deep Learning** (BDL) methods build on solid mathematical
foundations and hold promise for more reliable learned uncertainty
estimates [@wilson_case_2020]. Bayesian Neural Networks (BNN) are in
theory able to avoid the pitfalls of stochastic non-convex optimization
on non-linear tunable functions with many high-dimensional parameters
[@mackay1995probable]. In their original formulation, BNNs come with
high computational cost, since it involves learning a Gaussian
distribution for each weight in the network, effectively doubling the
number of parameters. The Bayesian approach consists of casting learning
and prediction as an inference task about hypotheses (uncertain
quantities, with $\theta$ representing all BNN parameters: weights $w$,
biases $b$, and model structure) from data (measurable quantities,
$$\mathcal{D}=\left\{\left(\mathbf{x}^{(n)}, y^{(n)}\right)\right\}_{n=1}^{N}=(\mathbf{X}, \mathbf{Y})$$
). Drawing on the ground-laying works of @denker1987large
[@mackay1992bayesian; @neal1992bayesian; @hinton1993keeping], the
"second-generation\" in BDL [@ghahramani2016history] is geared towards
finding practical and scalable approximations to the analytically
intractable Bayesian posterior (Eq.
[\[eq:intractable-posterior\]](#eq:intractable-posterior){reference-type="ref"
reference="eq:intractable-posterior"}).

$$P(\theta \mid \mathcal{D}, m)= \frac{P(\mathcal{D} \mid \theta, m) P(\theta \mid m)}{P(\mathcal{D} \mid m)}
\begin{aligned}
& \quad \displaystyle P(\mathcal{D} \mid \theta, m) & \scriptstyle \text{likelihood of } \theta \scriptstyle \text{ in model } m \\
& \quad \displaystyle P(\theta \mid m) & \scriptstyle \text{prior probability of } \theta \\
& \quad \displaystyle P(\theta \mid \mathcal{D}, m) & \scriptstyle \text{posterior of } \theta \scriptstyle \text{ given data } \mathcal{D}
\end{aligned}
\label{eq:intractable-posterior}$$ 

Generating a prediction for a new test input $x^{*}$ requires computing the conditional probability of $x^{*}$ given the data and model.
$$P(x^{*}\mid\mathcal{D}, m) = \int P(x^{*}\mid\mathcal{D},\theta,m) \underbrace{P(\theta \mid \mathcal{D}, m)}_{posterior}  d\theta$$
To compute the *predictive distribution*, again the posterior
distribution is required, whose integral via marginalization over the
parameters is typically very high-dimensional and typically intractable:
$$P(\mathcal{D}, m) = \int P(\mathcal{D},\theta,m) d\theta$$
**Variational Inference** (VI) is a Bayesian modeling technique employed
by a majority of BDL methods that aim to circumvent the *inference
problem*. The key idea consists of approximating the intractable
posterior distribution $P(\theta \mid \mathcal{D}, m)$ with a simpler
(though conjugate), tractable distribution $q(\theta)$. Specifically, by
minimizing $KL(q||p)$, the Kullback--Leibler (KL) divergence between the
approximating distribution and the replaced true posterior, one can
perform Bayesian approximate inference under the guarantees of
maximizing the *evidence lower bound* (ELBO) w.r.t. $\theta$ given data.

Diverse strategies have been proposed to principally and practically
approximate the posterior distribution for beneficial uncertainty
estimation. In what follows we will focus on methods that have seen more
widespread adoption given their ability to scale both in network
architecture and dataset size. In this, we follow the ensembling
categorization of @ashukha_pitfalls, who discern two main strategies:

1.  Obtaining snapshots of model parameters

2.  Introducing stochasticity in the computation graph

**The weight snapshots direction** aims to find different sets of NN
weights during training. Within this group, three sub-strategies exist:
(i) the traditionally resource-expensive yet empirically effective
***Deep Ensemble*** trains independent sets of weights
[@lakshminarayanan2016simple], (ii) snapshots are connected during
different stages of training
[@huang2017snapshot; @garipov_loss_2018; @maddox2019simple], or (iii) a
sampling process such as Markov Chain Monte-Carlo
[@gilks1995markov; @zhang_cyclical_2019; @hoffman_langevin_2019] is
used. Predictions are averaged across the snapshots during evaluation
where model uncertainty can be estimated.\
**The stochastic computation-graph direction** involves the introduction
of noise over weights and/or activations during training, where each
stochastic noise variant represents a model within the ensemble, and at
inference time predictions are averaged over the members of the
ensemble. Notable examples include ***Monte Carlo Dropout***
[@gal_dropout_2016], Batch Normalization
[@atanov_uncertainty_2018; @teye_bayesian_2018], and Stochastic
Variational Inference
[@graves2011practical; @Blei_VI_2017; @farquhar2019radial].\
In our benchmarking study we select at least 1 representative method
(denoted by cursive emphasis) from each of the above categories,
motivating a cross-category comparison and analyzing their
individual-joint effectiveness in modeling predictive uncertainty.

Predictive Uncertainty Methods {#section:preduquant}
------------------------------

We will first introduce each method by explaining the algorithm,
followed by advantages or identified shortcomings, with subsequent
method extensions from the same procedure category. Finally, we will
zoom in on how to quantify uncertainty using each method.

### Monte Carlo Dropout {#section:mcd}

The seminal work of @gal_dropout_2016 on Monte Carlo Dropout (MC
Dropout, MCD) proposes efficient model uncertainty estimation by
exploiting dropout regularization as an approximate VI method. The
authors reason that dropout training approximately integrates over model
parameters by randomly masking (setting to 0) weight matrices, which is
equivalent to drawing samples from a Bernoulli distribution given a
fixed dropout probability. Concretely, for an $L$ layers deep NN with
weights $W_{l}$ they define a variational Bernoulli distribution with
$\Phi$ dropout rates (Eq.
[\[bernoulli-q\]](#bernoulli-q){reference-type="ref"
reference="bernoulli-q"}), where a Gaussian matrix $G_{l}$ is multiplied
with a diagonal matrix of Bernoulli random variable realizations
(dropout masks), $diag[\mathbf{z}]$, drawn from
$\operatorname{Bernoulli}(\boldsymbol{\theta} ; \Phi)$ for each set of
weights $W_{l} = G_{l} diag[\mathbf{z}]$.
$$P(\boldsymbol{\theta} \mid \mathcal{D}) \approx q(\boldsymbol{\theta} ; \Phi)=\operatorname{Bernoulli}(\boldsymbol{\theta} ; \Phi) \label{bernoulli-q}$$
Additionally, they show that a Deep NN with dropout applied before every
weight layer mathematically approximates a deep Gaussian Process (GP)
[@rasmussen2003gaussian]. This is an important comparison as GPs have
desirable properties for principled uncertainty estimation.

In practice, the MCD procedure boils down to (i) applying dropout on all
non-linear layers' weights, and (ii) activating dropout both during
training and evaluation, wherein the latter predictions are averaged
from $T$ stochastic forward passes with different dropout masks to
obtain an approximate posterior.

Quantifying "epistemic\" *model uncertainty* using MCD involves applying
dropout both during training and evaluation. In the latter case, $T$
stochastic weights are sampled from the variational Bernoulli
distribution $\hat{\theta}_{t} \sim q(\boldsymbol{\theta})$ to calculate
the lower-order moments of the approximate Gaussian posterior,
respectively the predictive mean and variance (Eq.
[\[eq:predmeanvar\]](#eq:predmeanvar){reference-type="ref"
reference="eq:predmeanvar"}). $$\begin{split}
\hat{\mu}_{pred}(\mathbf{x}^{*}) = \frac{1}{T} \sum_{t=1}^{T} P(y^{*} | \mathbf{x}^{*}, \hat{\theta}_{t}) \\
\hat{\sigma}_{pred}(\mathbf{x}^{*}) = \frac{1}{T} \sum_{t=1}^{T}  [ P(y^{*} | \mathbf{x}^{*}, \hat{\theta}_{t})-\hat{\mu}_{pred}]^{2}
\end{split}
\label{eq:predmeanvar}$$

MCD's simplicity and computational tractability, i.e. dropout training
is a standard DL practice and prediction only requires 1 model from
which to sample (in parallel), has made it one of the most popular
predictive uncertainty methods. However, there are some known
limitations with MCD that have been explored in further works. An
important shortcoming of VI, and in consequence MCD in
@gal_dropout_2016's formulation, is that they are known to underestimate
predictive variance [@turnersahani2011]. Whereas @gal_dropout_2016
originally grounded the Bayesian interpretation of dropout in
Variational Inference, @nalisnick2018dropout decouple dropout from
inference and suggests a generalization of multiplicative noise to
structured shrinkage priors. Their extension is dependent on the
efficiency of Markov chain Monte Carlo (MCMC) sampling algorithms, which
is why we do not consider it. We will touch on a selection of
representative extensions in further subsections
([1.2.3](#section:concretedrop){reference-type="ref"
reference="section:concretedrop"},
[1.2.4](#section:heteroscedastic){reference-type="ref"
reference="section:heteroscedastic"}).

### Deep Ensemble {#section:deepensembles}

Deep Ensemble [@lakshminarayanan2016simple] (DE) involves independently
training multiple probabilistic NNs with different random weight
initializations and aggregating predictions from individual models. The
empirical success of DE demonstrated that combinations of NNs trade-off
computational resources for beneficial uncertainty estimation,
robustness to dataset shift, and model quality improvements. As a
downside, it has higher computational and memory complexity, since you
need to train and store $M$ models. A recent benchmarking survey
[@ovadia2019trust] found DEs of a relatively small size ($M$=5) to be
more robust to dataset shift and perform the best all-around compared to
other popular BDL methods. In comparison to MC Dropout, DEs are treated
as a uniformly-weighted Gaussian Mixture model, to which the formula for
predictive variance is adapted: $$\hat{\sigma}_{pred}(\mathbf{x}^{*}) = 
\frac{1}{M}\sum_{m}\left(\sigma_{\theta_{m}}^{2}(\mathbf{x^{*}})+\mu_{\theta_{m}}^{2}(\mathbf{x^{*}})\right)-\mu_{*}^{2}(\mathbf{x^{*}})
\label{eq:DE}$$ The empirical performance increase of ensembles can be
attributed to the diversity of (uncorrelated) errors between ensemble
members. In the absence of diversity, ensembles lack good posterior
approximation and for this reason, ensemble diversity promotion is a
promising avenue for further improvements
[@jain2020maximizing; @brazowski_collective_2020]. The interplay between
ensembling and regularization, \"the effect of a prior\", warrants more
thought since not regularizing risks overfitting, while too strong
regularization risks constraining diversity (cf. Subsection
[1.4](#complementarity){reference-type="ref"
reference="complementarity"}).

### Concrete Dropout {#section:concretedrop}

As referred to in Section [1.2.1](#section:mcd){reference-type="ref"
reference="section:mcd"}, the original MC Dropout definition with
fixed-rate Bernoulli variational distribution suffers from uncertainty
underestimation and miscalibration. To obtain well-calibrated
uncertainty estimates, @Osband2016RiskVU made a case for manually tuning
layer-wise dropout probability rates, since the dropout probability
characterizes the overall posterior uncertainty. However, this
grid-search is prohibitively expensive for deeper models.

@gal2017concrete proposes a **Con**tinuous-dis**crete** distribution
relaxation to adapt and optimize the dropout probability $p$ as a
variational parameter using standard gradient descent. By taking
advantage of the reparametrization trick, the Concrete distribution
approximation $\tilde{\mathbf{z}}$ of the original Bernouilli random
variable $\mathbf{z}$ conveniently parametrizes to a simple sigmoid
distribution allowing for gradient-based optimization. Given a low
temperature $r$ (0.1) and a uniform random noise variable $\mathbf{u}$,
the expression varies with respect to $p$, which if $p>>$0.5, sigmoid
produces accelerated by a factor 10 a value approaching 1.
$$\tilde{\mathbf{z}}=\operatorname{sigmoid}\left(\frac{1}{r} \cdot(\log p-\log (1-p)+\log\mathbf{u}-\log (1-\mathbf{u}))\right)$$
Concrete Dropout promises better-calibrated uncertainties at an almost
negligible cost, consequently reducing experimentation time.

### Heteroscedastic Extensions {#section:heteroscedastic}

@kendall2017uncertainties
[@kwonuncertaintyclassification; @xiao_quantifying_2018] proposed
similar approaches to extend MC Dropout predictive uncertainty to allow
measuring uncertainty information from different sources.\
Estimating input-dependent, "heteroscedastic aleatoric\", *data
uncertainty* (detail Subsection
[\[section:dataquant\]](#section:dataquant){reference-type="ref"
reference="section:dataquant"}) requires slightly modifying the model's
architecture and objective function following @kendall2017uncertainties.
Firstly, the output layer of model $f_{\hat{\theta}}$ is extended with a
set of learnable variance variables $\boldsymbol{\sigma}$ per unique
class output. The model's output logits, $\mathbf{v}$, are sampled from
the stochastic output layer parametrized by
$\mathcal{N}(f_{\hat{\theta}}(x), diag(\boldsymbol{\sigma}(x)^{2}))$.
This model adaptation will be referred to as the *heteroscedastic
model*. *Fig.* [\[fig:arxs\]](#fig:arxs){reference-type="ref"
reference="fig:arxs"} visualizes the difference in output layer design.

Next, it requires incorporating a residual *heteroscedastic loss*:
$$%\resizebox{0.9\hsize}{!}{
\displaystyle \mathcal{L}_{\mathrm{HET}}(\mathbf{\hat{\theta}})= \sum_{i=1}^{N} \log \frac{1}{T} \sum_{t=1}^{T} \exp \left({\mathbf{v}}_{i, c}^{(t)}-\log \sum_{k} \exp \mathbf{v}_{i,k}^{(t)}\right) + \log T
%}
\label{lossattenuation}$$ with $N$ the number of training examples
passing through an instance $t$ of the model
$f_{\hat{\theta}_{t}}\left(x\right)$ + $\boldsymbol{\sigma}^{(t)}$ to
generate for example $i$ a sampled logit vector $\mathbf{v}_{i}^{t}$,
where predicted value for class $k$, $\mathbf{v}_{i,k}^{(t)}$, and $c$
the index of the ground truth class. By learning to predict log variance
with $T$ dropout-masked samples, the model will be able to predict high
variance (uncertainty) for inputs where the predictive mean is far
removed from the true observation, which by design has a smaller effect
on the total loss. This uncertainty modeling method is referred to as
*Learned Loss Attenuation*.

Uncertainty Estimation {#section:uquant}
----------------------

In this Subsection, we will introduce sources of uncertainty, how
uncertainty is quantified in practice, followed by a categorization of
uncertainty.

### Total Uncertainty

Classification models trained by minimizing negative log-likelihood
(i.e. cross-entropy) quantify global uncertainty over class outcomes
with entropy (H) over logits. Therefore, the entropy of the posterior
predictive distribution can be determined a measure of both data
uncertainty and model uncertainty [@hullermeier2019aleatoric]. In our
definition of predictive uncertainty, we consider both **calibration**
and **robustness**. Model misspecification, noisy data or supervision
all contribute to the total uncertainty.\
Decomposing total uncertainty into the different sources is beneficial
for determining actions to evaluate the room for improvement. Model
uncertainty is reducible by collecting more data, whereas data
uncertainty cannot be decreased by model refinements or including more
data.

### Model Uncertainty

**Epistemic uncertainty** presents the inherent "uncertainty\"
[@Osband2016RiskVU] of the model with regards to the true values for its
parameters and structure after having seen the training data. The model
will communicate ignorance because of lack of knowledge, evidenced by a
broad posterior over parameters. In principle, this quantity of
uncertainty can be reduced by feeding more data, choosing a more
expressive model, or by finding more appropriate values for the
hyperparameters. The quantity is hypothesized (e.g.
@seedat2019calibrated) to increase when presented with test inputs far
removed from the training distribution.\
*Mutual Information* (MI) [@smith_understanding_2018] has been proposed
as a separate measure of epistemic uncertainty, contrasting to
predictive entropy which is high given any model uncertainty or data
noise. Intuitively, the measure captures the amount of information that
would be gained about model parameters through knowledge of the true
outcome (Eq. [\[eq:MI\]](#eq:MI){reference-type="ref"
reference="eq:MI"}).
$$\operatorname{MI}(\boldsymbol{\theta}, y \mid \mathcal{D}, \mathbf{x^{*}})= H(y \mid \mathbf{x^{*}}, \mathcal{D})-\mathop{\mathbb{E}}_{p(\theta \mid \mathcal{D})} [H(y \mid \mathbf{x^{*}},\mathbf{\theta})]
\label{eq:MI}$$

### Data Uncertainty [\[section:dataquant\]]{#section:dataquant label="section:dataquant"}

**Aleatoric uncertainty** captures the inherent stochasticity and noise
in data. Moreover, it cannot be explained away when feeding the model
more data. It can be further decomposed into a *homoscedastic*
component, which represents constant noise over inputs such as the
numerical accurateness of a measuring device, and *heteroscedastic*
uncertainty representing input-dependent noise generated by the data by,
for instance, class overlap, complex decision boundaries or label noise.
Including the quantification of heteroscedastic data uncertainty allows
for the expression of instance-level uncertainty. Even when having
frequently observed a sample during training, instance-level data noise
should be expressed together with the best possible prediction.

### Uncertainty categorization {#section:uncertainty}

Below follows a categorization of the uncertainty quantities within the
scope of the experiments. To estimate for a new test sample $x^{*}$ the
prediction and uncertainty of model $f_{\hat{\theta}}(x^{*})$ we
typically seek to obtain the predictive posterior distribution
$P(y^{*} | x^{*}, \hat{\theta})$ over class membership probabilities
with $y^{*}_{k} \in \{1,\ldots, K\}$.

For MC Dropout at inference time, we presume
$P(y^{*} | x^{*},\hat{\theta}) \approx \frac{1}{T}\sum_{t=1}^{T} P(y^{*} | x^{*}, \hat{\theta}_{t})$,
with prediction obtained after applying softmax/sigmoid function for
sample $t$, $\hat{p}_{t}= P(y^{*} | x^{*}, \hat{\theta}_{t})$, and
predictive mean $\bar{p}=\frac{1}{T} \sum_{t=1}^{T} \hat{p}_{t}$. For
Deep Ensemble, the above notations would require a change from $T$ to
$M$, but for consistency over quantity formulas, we maintain $T$ to
denote posterior sampling. For ease of notation, we define a helper
entropy function on
$H(x^{*},z) = -\sum_{k=1}^{K} P(y_{k}|x^{*}, z) \log P(y_{k}|x^{*}, z)$.

$$\begin{aligned}
\textit{Quantity} \qquad & \phantom{=}  \textit{Formula } \nonumber\\
\cline{1-2}
\text{\small{\textbf{Softmax-score}}} \qquad & \phantom{=} \displaystyle S = \argmax_{k} \frac{\exp f_{\hat{\theta}, k}(x^{*})}{\sum_{i=1}^{K} \exp f_{\hat{\theta},i}(x^{*})} \\ 
\text{\small{\textbf{Predictive Entropy}}} \qquad & \phantom{=} H_{pred} = H(x^{*},\hat{\theta})\\ 
\text{\small{\textbf{Mutual Information}}} \qquad & \phantom{=} I=  H_{pred} - \frac{1}{T} \sum_{t=1}^{T} H(x^{*},\hat{\theta}_{t})  \\ 
\text{\small{\textbf{Model Uncertainty}}} \qquad & \phantom{=} \hat{\sigma}_{model}=\frac{1}{T} \sum_{t=1}^{T}  \left( \hat{p}_{t}-\bar{p}\right)^{2}\\
\text{\small{\textbf{Data Uncertainty}}} \qquad & \phantom{=} \hat{\sigma}_{data}= \frac{1}{T} \sum_{t=1}^{T} \frac{1}{K} \sum_{k=1}^{K}  \boldsymbol{\sigma}_{k}^{(t)}(x^{*})\end{aligned}$$

For any classification model, it is possible to compute the
softmax-score and predictive entropy. For multi-label classification,
softmax-score does not take into account multiple winning classes and a
standard approximation would be to average over the sigmoid-scaled
probabilities of predicted classes.

Model uncertainty can be quantified with Monte Carlo integration or the
aggregation of individual models. In practice, it is quantified by
either (a) calculating the average sigmoid/softmax variance over the
predictive mean from MC samples or (b) computing the total variance from
an ensemble mixture distribution (Eq.
[\[eq:DE\]](#eq:DE){reference-type="ref" reference="eq:DE"}). Changing
to the heteroscedastic extensions allows to quantify data uncertainty.
More specifically, data uncertainty is quantified with as surrogate the
average over variance logits $\boldsymbol{\sigma}$ (see *Fig.*
[\[fig:arxs\]](#fig:arxs){reference-type="ref" reference="fig:arxs"}).
Whenever ensembling is applied where a single model estimates a
quantity, one typically averages over the ensemble components'
uncertainty.
