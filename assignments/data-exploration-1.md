---
title: 'PSYC 5720 --- Computational Neuroscience'
subtitle: 'Data Exploration 1: Choosing a Project'
documentclass: scrartcl
fontsize: 11pt
linkcolor: blue
geometry: letterpaper, margin=1in
header-includes:
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
---

The overall goal of this assignment is for you to explore in depth one of the theoretical approaches covered in this class by analyzing a public data set or data of your own. There are five stages to the project, culminating in a short presentation given to the rest of the class.

- **Choose a group and topic**: due 2/29
- **Present a journal club article**: 3/12 and 3/14
- Document the data and/or model: due 3/28
- Formulate a hypothesis: due 4/11
- Present the results: 4/25 and 5/2

*Assignment*: With your group (max 4 members), choose a project topic and one of the associated journal articles. By March 14, let your instructor know who is in your group and which article you plan to discuss. Be prepared to present the article to the rest of the class on 3/21 or 3/23. A guideline for the presentation is at the end of this document.

## Choosing a project

Your project should focus on one of the main theoretical approaches we have covered in class. Here are your options, along with some associated journal articles. Each of the articles has a corresponding dataset available on the  [Collaborative Research in Computational Neurocience Data Sharing website](https://crcns.org). You will use these data in your project, so you may want to take a look at the CRCNS website to see how the data are organized when deciding which article/project to present. More advanced students may choose to use a different dataset from CRCNS or from their own research, but should pick an article that is mostly closely aligned with their project idea.

### Analyze neural responses to estimate receptive fields

A classical approach to studying neural processing is to characterize the receptive fields of individual neurons. Receptive fields are "encoding" models: they attempt to predict how a neuron will respond to (encode) an arbitrary stimulus, which is typically under experimental control. Most of the commonly used encoding models are linear-nonlinear cascade models. If you choose this project, your tasks will be to:

1. Decide how to represent the stimulus and response and define your encoding model mathematically.
2. Estimate the parameters of the model for individual neurons.
3. Test the model and goodness of fit by seeing if you can predict responses to novel stimuli.
4. Test a hypothesis of your choice.

These papers and datasets will work well with this project type.

- Scholl B, Tan AYY, Corey J, and Priebe NJ. (2013) Emergence of orientation selectivity in the mammalian visual pathway J. Neurosci. 33(26):10616-10624. [lgn-1](https://crcns.org/data-sets/lgn/lgn-1). You should be able to use a fairly simple linear encoding model and estimation techniques with these neurons.
- Touryan J, Felsen G, and Dan Y. (2005) Spatial structure of complex cell receptive fields measured with natural images, Neuron 45, 781-791. [pvc-2](https://crcns.org/data-sets/vc/pvc-2)
- Felsen G, Touryan J, Han F, and Dan Y. (2005) Cortical sensitivity to visual features in natural scenes, PLoS Biol. 3 (10), e342. [pvc-2](https://crcns.org/data-sets/vc/pvc-2)
- Amin N, Gill P, Theunissen FE. (2010) Role of the zebra finch auditory thalamus in generating complex representations for natural sounds. J Neurophysiol. 104(2):784-98 [aa-2](https://crcns.org/data-sets/aa/aa-2)
- Woolley SMN, Gill PR, Fremouw T, Theunissen FE (2009) Functional groups in the avian auditory system. J Neurosci 29(9):2780-93. [aa-2](https://crcns.org/data-sets/aa/aa-2). A simple linear model will work for many neurons, but you will need to use regularized linear regression to obtain good estimates.

### Build and test a decoder/classifier

A decoding model attempts to predict what stimulus was presented from the responses of one or more neurons. A special type of decoding model is the classifier, which predicts which one of a discrete number of stimuli was most likely to have been presented. Decoding models are also often applied to motor systems. If you choose this project, your tasks will be to:

1. Decide how to represent the stimulus/action and response and define your decoding model mathematically.
2. Train the decoder/classifier on a subset of the data.
3. Test how well the decoder/classifier can predict the stimulus/action given a novel response.
4. Test a hypothesis of your choice.

These papers and datasets should work well with this project:

- Wirth S, Baraduc P, Plante A, Pinede S, Duhamel J-R (2017). Gaze-informed, task-situated representation of space in primate hippocampus during virtual navigation. PLoS Biology. doi:10.1371/journal.pbio.2001045. [hc-12](https://crcns.org/data-sets/hc/hc-12)
- Kay, K. N., Naselaris, T., Prenger, R. J., & Gallant, J. L. (2008). Identifying natural images from human brain activity. Nature, 452(7185), 352-355. [vim-1](https://crcns.org/data-sets/vc/vim-1)
- Naselaris, T., Prenger, R. J., Kay, K. N., Oliver, M., & Gallant, J. L. (2009). Bayesian reconstruction of natural images from human brain activity. Neuron, 63(6), 902-915. [vim-1](https://crcns.org/data-sets/vc/vim-1)
- Feierstein CE, Quirk MC, Uchida N, Sosulski DL, Mainen ZF (2006) Representation of spatial goals in rat orbitofrontal cortex. Neuron 51(4):495-507. [ofc-1](https://crcns.org/data-sets/ofc/ofc-1)
-  Lakshminarasimhan KJ, Pouget A, DeAngelis GC, Angelaki DE, Pitkow X (2018) Inferring decoding strategies for multiple correlated neural populations PLos Comp Biol 14(9): e1006371. [stc-1](http://crcns.org/data-sets/vc/stc-1)
- Kepecs A, Uchida N, Zariwala H, Mainen ZF (2008). Neural correlates, computation and behavioural impact of decision confidence. Nature 455, 227–231. [ofc-2](http://crcns.org/data-sets/ofc/ofc-2)
- Nishimoto  S, Vu AT, Naselaris T, Benjamini Y, Yu B, Gallant JL (2011). Reconstructing visual experiences from brain activity evoked by natural movies. Current Biology, 21(19), 1641-1646. [vim-2](http://crcns.org/data-sets/vc/vim-2)
- Çukur T, Shinji N, Alexander GH, Gallant JL (2013). Attention during Natural Vision Warps Semantic Representation across the Human Brain. Nature Neuroscience 16 (6): 763–70. [vim-4](http://crcns.org/data-sets/vc/vim-4)

### Advanced: An analysis of your own design

You are welcome to pursue your own project idea if it is feasible to do in the allotted time. You will need to choose a relevant paper and get instructor approval before proceeding with this option. Some ideas for topics:

- Build a biophysical model of an interesting neuron type
- Characterize network dynamics of a neural population using neural manifolds or other dimensional reduction techniques
- Implement a computation (e.g. decorrelation, pattern matching, pattern completion) in an artificial neural network.

## Choosing a group

You may work on this project alone or in a group of up to 4 members. Groups work best if the skills of the members (i.e. programming, math, biology) are complementary. Agree early on about your expectations for when and how often to meet and on how to equitably divide up the work. Part of your grade will be based on your team's evaluation of your contribution.

## Presentation guidelines and rubric

Your presentation to the class will be in *journal club* format. The amount of time you are allotted will depend on the number of groups we have. It should consist of the following parts:

1. Introduce the paper: title, authors, what journal it was published in and when.
2. Clearly state the overarching problem or question the paper addresses.
3. Explain what the paper is seeking to do to address that problem/question.
4. Briefly outline the experimental design (study species, methodology, groups or conditions) as it relates to the central hypothesis.
5. Go through each of the figures and explain what they show. Stay focused on the big picture. Say what the authors are claiming and then explain how the data support that claim (or don't).
6. Summarize the results and give your opinion.
7. Take questions
