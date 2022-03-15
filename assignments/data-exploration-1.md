---
title: 'PSYC 5720 --- Computational Neuroscience'
subtitle: 'Data Exploration Assignment: Choosing a Data Set'
documentclass: scrartcl
fontsize: 11pt
linkcolor: blue
geometry: letterpaper, margin=1in
header-includes:
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
---

The goal of this assignment is to help you choose a project for data exploration activities in this course.

### What kinds of data should I be looking for?

Recall that our working definition of a computation is some kind of transformation between input and output. In this course, we're interested in the kinds of computations the brain does and how they are implemented in neural circuits, so we want to know what is going on in those circuits while the computation is happening. This framework boils down to two main guidelines:

The data set you choose has to involve recordings of neural activity. This rules out purely behavioral data.

The experiment needs to address a computational problem. Almost always this means that stimuli (inputs) are being presented to the subject under experimental control, the subject's actions (outputs) are being measured, or both.

The questions in the assignment will help you decide how a data set fits into this framework. Check with your instructor if you're still not sure.

You are not committed to using this dataset for your final project. Rather, this is an exercise in learning how public data sets are (and aren't) organized.

### How do I find the data?

For this exercise, we'll be looking at data sets hosted on the [Collaborative Research in Computational Neurocience Data Sharing website](https://crcns.org). Most of the data sets are from animals and using extracellular electrophysiology, but there are also EEG, fMRI, and intracellular data sets.

To get you started, I've provided links to some specific CRCNS data sets, organized by the kinds of computational questions the data address. You should feel free to use pretty much any of the other data sets as long as they fit the guidelines.

#### Sensory coding

How is sensory information represented and processed in the brain? How does the brain detect and discriminate between different stimuli?

- [pvc-1](https://crcns.org/data-sets/vc/pvc-2): Single-unit extracellular recordings from cat primary visual cortex (V1) in response to random bar stimuli. V1 is the first station for visual information in the cortex. It represents relatively simple visual features like orientation and direction.
- [pvc-8](https://crcns.org/data-sets/vc/pvc-8): Simultaneous extracellular recordings from multiple neurons in monkey V1 in response to natural images and gratings.
- [pvc-7](https://crcns.org/data-sets/vc/pvc-7): Calcium imaging of many neurons simultaneously in mouse V1, in response to gratings.
- [v2-1](https://crcns.org/data-sets/vc/v2-1): Single-unit extracellular recordings from monkey V2. V2 is above V1 in the visual processing hierarchy and is thought to be involved in processing more complex visual features.
- [vim-1](https://crcns.org/data-sets/vc/vim-1): fMRI of human visual areas in response to natural scenes. fMRI has much lower spatial and temporal resolution compared to single-unit recordings and calcium imaging, but it can be applied in humans and provides a broad view of activity in multiple brain areas.
- [ac-3](https://crcns.org/data-sets/ac/ac-3): Simultaneous extracellular recordings from multiple neurons in rat A1 in response to synthetic auditory stimuli. For those interested in the auditory modality.
- [aa-2](https://crcns.org/data-sets/aa/aa-2): Single-unit recordings from the zebra finch auditory cortex, in response to zebra finch songs and synthetic stimuli.

For other data sets related to this question, look in the visual cortex, auditory cortex, somatosensory cortex, thalamus, and retina folders.

#### Spatial navigation

How does an animal know where it is relative to important locations in its environment? This is a bit like sensory coding, in that we are asking how neural activity relates to an external variable, but in contrast, the location is (typically) under the control of the animal rather than the experimenter. The hippocampus is critical to this computation, along with a number of associated temporal areas.

- [hc-2](https://crcns.org/data-sets/hc/hc-2): Simultaneous multichannel broadband recordings from the CA1 region during open field tasks. The data include both spikes and local field potentials.
- [hc-6](https://crcns.org/data-sets/hc/hc-6): Extracellular recordings from CA1 and CA3 in rats performing a maze navigation task.
- [hc-12](https://crcns.org/data-sets/hc/hc-12): Single-unit extracellular recordings from rhesus macaques performing a virtual navigation task.

#### Motor planning and execution

How does the brain generate the correct patterns of activity to drive muscles as animals perform complex tasks?

- [pmd-1](https://crcns.org/data-sets/motor-cortex/pmd-1): Extracellular recordings of neurons in monkey premotor and primary motor cortex during a reaching task.
- [alm-1](https://crcns.org/data-sets/motor-cortex/alm-1): Extracellular recordings from a mouse motor area during a tactile decision task.

#### Working memory

How does the brain temporarily store information during tasks?

- [pfc-3](https://crcns.org/data-sets/pfc/pfc-3): Single-unit recordings from monkey prefrontal cortex during a visual working memory task
- [pfc-5](https://crcns.org/data-sets/pfc/pfc-5): 64-channel scalp EEG recordings from humans during a visuospatial working memory task


### What's the assignment?

Explore a few data sets on CRCNS. Choose one that interests you. Read at least one of the associated papers. Write brief responses to the following questions and submit as a PDF or Word document on Collab:

1. Which data set did you choose and why?
2. What computational problem was the paper associated with this data set trying to address?
3. What was the main finding of the paper?
4. What method was used to record brain activity? What kind of data (time series, point process, etc) was generated?
5. How are the neural recordings stored? Do you think it will be easy to read them into Python?
6. Did the experiment control stimuli or measure behavior during the recording? How is information about the stimulus/behavior stored in the data repository?
7. What do you think you might want to look at in this data set? Your idea doesn't have to be fully fledged, but see if you can brainstorm a bit.
