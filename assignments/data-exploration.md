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

The overall goal of this assignment is for you to explore in depth one of the theoretical approaches covered in this class by analyzing a public data set or data of your own. There are four stages to the project, culminating in a short presentation given to the rest of the class.

- **Choose a group and a project**: due 3/24
- Document the data and/or model: due 3/31
- Formulate a hypothesis: due 4/12
- Present the results: 4/21 and 5/3

*Assignment*: With your group (max 4 members), write a paragraph identifying the project type and data set you chose, and a brief description of what you intend to do. Submit through Gradescope on Collab.

## Choosing a group

You may work on this project on your own or in a group of up to 4 members. If you work in a group, choose members who have complementary skills (e.g. programming, biology, math) and who can work effectively together. Agree about expectations for when you will meet and how you will divide up the work.

## Choosing a project

Your project should focus on one of the main theoretical approaches we cover in class. Here are your options, along with some recommended data sets. The data sets come from the the [Collaborative Research in Computational Neurocience Data Sharing website](https://crcns.org) and can be found in the `shared-data` folder on Rivanna. Each directory will include documentation about how the data were collected and organized, along with references to published articles about the experiment.

### Analyze neural responses to estimate receptive fields

A classical approach to studying neural processing is to characterize the receptive fields of individual neurons. Receptive fields are "encoding" models: they attempt to predict how a neuron will respond to (encode) an arbitrary stimulus, which is typically under experimental control. Most of the commonly used encoding models are linear-nonlinear cascade models. If you choose this project, your tasks will be to:

1. Decide how to represent the stimulus and response and define your encoding model mathematically.
2. Estimate the parameters of the model for individual neurons.
3. Test the model and goodness of fit by seeing if you can predict responses to novel stimuli.
4. Test a hypothesis of your choice.

These data sets should work well with this project:

- `crcns/lgn-1`: spiking responses of LGN neurons in the mouse to drifting gratings. You should be able to use a fairly simple linear encoding model and estimation techniques with these neurons.
- `crcns/aa-2`: zebra finch auditory neurons from a variety of brain regions stimulated with individual songs and synthetic noise. A simple linear model will work for many neurons, but you will need to use regularized linear regression to obtain good estimates.
- `zf/noise-invariance`: zebra finch auditory neurons stimulated with auditory scenes comprising foreground zebra finch songs added to a complex background mimicking the sound of a zebra finch colony. These data were collected in the Meliza lab, so we can provide a lot of assistance understanding the structure. You may need a more complex nonlinear model and estimation techniques for these cells, however.

### Build and test a decoder/classifier

A decoding model attempts to predict what stimulus was presented from the responses of one or more neurons. A special type of decoding model is the classifier, which predicts which one of a discrete number of stimuli was most likely to have been presented. Decoding models are also often applied to motor systems. If you choose this project, your tasks will be to:

1. Decide how to represent the stimulus/action and response and define your decoding model mathematically.
2. Train the decoder/classifier on a subset of the data.
3. Test how well the decoder/classifier can predict the stimulus/action given a novel response.
4. Test a hypothesis of your choice.

These data sets should work well with this project:

- `crcns/hc-28`: Recordings from hippocampus regions CA1 (primarily dorsal CA1 and some intermediate CA1 recordings) and medial prefrontal cortex (PFC, prelimbic and infralimbic regions) from three male Long-Evans rats learning a continuous alternation W-track task.
- `crcns/vim-1`: fMRI of human visual areas in response to natural scenes. fMRI has much lower spatial and temporal resolution compared to single-unit recordings and calcium imaging, but it can be applied in humans and provides a broad view of activity in multiple brain areas.
- `zf/noise-invariance`: same data as for the encoding model. You could try to decode the spectrogram of the foreground stimulus or its identity.

### Simulate intracellular dynamics of a neuron type

The voltage dynamics of individual neurons can be simulated using the biophysical framework developed by Hodgkin and Huxley. These models consist of a set of ordinary differential equations corresponding to the membrane voltage and the states of the activation/inactivation gates for voltage-gated currents. If you choose this project, your tasks will be to:

1. Pick a neuron type that has been studied using slice electrophysiology and determine which currents (ion channels) to include in the model.
2. Search [Channelpedia](https://channelpedia.epfl.ch/) to find equations for the currents/channels in your cell type.
3. Implement the model in [Brian](https://briansimulator.org) (recommended) or [NEURON](https://www.neuron.yale.edu/neuron/) (for more complex multicompartment models).
4. Use the model to generate simulated responses and compare them to published results.
5. Test a hypothesis of your choice.

Some cell types that would work well for this project:

- Layer 2/3 pyramidal cell in barrel cortex
- Cerebellar Purkinje cell
- Lateral Pyloric cell of the crab stomatogastric ganglion

### Implement a computation or dynamical behavior using a neural network

Networks of neurons can also be simulated using differential equations, usually with more abstract dynamics than a detailed biophysical model, but including synaptic connections within the network. Simple networks can exhibit interesting dynamical behaviors like stochastic resonance, or implement neural computations like decorrelation, pattern matching, and pattern completion. If you choose this project, your tasks will be to:

1. Choose a computation of interest. Define input and output structure.
2. Decide on a network architecture (e.g. feedforward, recurrent, rate-based, spiking) and define the equations.
3. Decide how to set free parameters (e.g. machine learning, randomized)
4. Test whether the network can implement the computation.

### An analysis of your own design

You are welcome to pursue your own project idea if it is feasible to do in the allotted time. You will need to get instructor approval before proceeding with this option.

## Part 2: Documenting the data or model

Encoding and decoding models: write a python module that will load the stimulus and response data from the data repository into a data structure or structures that will allow you to estimate the parameters of the model.

Biophysical model: submit a 1-page document with a brief description of the cell type and the currents you intend to include.

Network model: submit a 1-page document describing the computation you intend to implement, how you will structure the input and output, and what kind of network you will use.

## Part 3: Formulating a hypothesis

## Part 4: Presenting the analysis

public data set to address a specific hypothesis about how the brain performs computations. Given the time constraints of the class, you are only expected to make progress toward this goal, by pursuing a specific aim that you defined in your proposal.

Your submission will consist of two parts: code that you push to your github repository, and a report that describes your results. The code will account for 40% of the assignment credit, and the report for 60%.

# Code

Your github repository will need to contain a notebook that generates the figure(s) you present in your report. This notebook must be at the top level of the repository and be clearly named. I will evaluate your submission by cloning the repository, following your instructions in `README.md` and/or `data/README.md` to retrieve the data set, and then executing the notebook. Your notebook needs to work for you to receive full credit,  sure that someone following your instructions with a clean install can duplicate your results. I will mostly be evaluating this part of the assignment based on results, but 10% of your score will reflect whether your code is readable and appropriately documented.

# Report

Your report will be structured like an abbreviated scientific paper. This should be around 5 pages in length, with 1-inch margins, submitted as a PDF to Collab. Work that is of high quality that adheres to the guidelines, and with few mistakes in grammar, will receive full credit.

The report should begin with a title and a list of authors, and then the following sections, with the indicated headings.

## Introduction

The introduction can be based off your proposal. You need to define the overarching goal/question you are addressing in a way that emphasizes its significance to understanding neural computations and what is known already in the field. Briefly introduce your data set and clearly state a hypothesis and how it relates to the data. Finally, introduce the specific analysis you performed and how it relates to testing the hypothesis.

## Results

Succinctly describe the specifics of the analysis you performed and the results. You need to have at least one figure, which must be captioned with a detailed legend, and referenced in the main text of the report. Always use past tense when describing results.

## Discussion

Interpret your results in light of your hypothesis. Describe any limitations or unexpected outcomes, and summarize what the next step would be in addressing the hypothesis or general research question.

## References

You should reference at least 3 peer-reviewed primary research papers or reviews in your report. In the text, use parenthetical author-date citations, like (Meliza et al., 2019), and then provide a list of full references in this section. Each reference should include the authors, the title, the year of publication, the journal, and sufficient information to locate the article in the journal (a DOI, volume:start--end, or both). You can use whatever format you prefer as long as all of the required information is present. Every reference in this section needs to correspond to an in-text citation and vice versa. You need to cite the data set you used, using the form requested by the authors on the CRCNS website.

## Acknowledgments

Acknowledge the experimenters who collected the data you used, and any assistance you received from classmates not on the author list.
