
# Computational Neuroscience

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/melizalab/comp-neurosci.git/master)

This repository contains instructional materials for PSYC 5270, a course I teach on computational systems neuroscience at the University of Virginia. Students in this course learn how to process neuroscience data and model the way the brain processes, stores, and generates information. They also gain expertise in using scientific programming (specifically Python and its ecosystem of numerical and graphics libraries) to perform analyses and build models.

The current syllabus is [here](resources/syllabus.pdf).

## Getting started

### Cloud

The easiest way to run the exercises is to use [mybinder](https://mybinder.org). This will ensure that you have the latest version of the notebooks, all the data files, and the correct versions of required libraries. Click the badge at the top of this page to start a session. Note that this site does not save your work, so you have to be careful to download your `ipynb` files after you finish a session.

### Local

You should be able to run the notebooks locally using [uv](https://docs.astral.sh/uv/) to manage dependencies and virtual environments. After cloning the repository, the following command will launch the jupyter lab notebook server:

``` shell
uv run --with jupyter jupyter lab
```

If the interactive plots and widgets in some of the earlier notebooks give you a javascript error in the browser, you may need to install the jupyter-matplotlib extension with `uv run --with jupyter jupyter labextension install jupyter-matplotlib@0.11.8`. This requires a working copy of npm and nodejs, which you can install using your system package manager. 

Make sure you work on a copy of the notebook (go to `File/Make a Copy...` in the notebook) that you name with your UVA computing ID; otherwise you may run into conflicts if you try to pull updates to the notebooks from the github repository.

## Shared installation

Instructors may wish to have a single installation of the code and data to be shared by multiple users. These users will See `resources/

If you have a These instructions should work on any operating system to give you a working Python environment with all the required packages.

Install the Python 3.x version of [anaconda](https://www.anaconda.com/distribution/) (or [miniconda](https://conda.io/en/latest/miniconda.html) if you are comfortable using the shell). Run the following commands in a terminal, **one at a time** so that you can stop and fix any errors.

``` shell
conda create -n comp-neurosci python=3.9.7 numpy scipy pandas matplotlib notebook cython ipywidgets ipykernel
conda activate comp-neurosci
pip install -e .
python -m ipykernel install --user --name comp-neurosci --display-name "comp-neurosci"
```

When you run Jupyter, you will have the option of selecting the `comp-neurosci` kernel, which should have all of your software dependencies.


By default, the notebooks will load pregenerated data from files in the `data` subdirectory of this repository. If you are running a course and
