
# Computational Neuroscience

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/melizalab/comp-neurosci.git/master)

This repository contains instructional materials for PSYC 5270, a course I teach on computational systems neuroscience at the University of Virginia. Students in this course learn how to process neuroscience data and model the way the brain processes, stores, and generates information. They also gain expertise in using scientific programming (specifically Python and its ecosystem of numerical and graphics libraries) to perform analyses and build models.

The current syllabus is here.

## Getting started

### Local: system packages

Install Python 3.5+ and jupyter-notebook using your system package manager. Then create a virtualenv and link it to your notebook server as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=comp-neurosci
scripts/fetch_data.sh
jupyter-notebook
```

To restart the notebook server (e.g. after rebooting), just run `source venv/bin/activate && jupyter-notebook` from the package

### Local: anaconda

These instructions are a work in progress. Install [anaconda](https://docs.anaconda.com/anaconda/install/) on any of the major operating systems (including Windows).

### Cloud

Click the binder badge above to run the exercises on [mybinder](https://mybinder.org). Note that this site does not save your work, so you have to be careful to download your `ipynb` files after you finish a session.
