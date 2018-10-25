
# Data Science for Neuroscientists

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/melizalab/comp-neurosci.git/master)

This repository contains instructional materials for learning scientific programming and data science skills in neuroscience. This is a work in progress, but the following modules are complete:

- how to represent and store observations of neurons
- descriptive statistics of neural spike trains

## Getting started

### Local virtualenv deployment

Requirements: python 3.5 or greater, jupyter notebook

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=comp-neurosci
scripts/fetch_data.sh
jupyter-notebook
```

### Cloud-based deployment

Click the binder badge above to run the exercises on [mybinder](https://mybinder.org).

See `docs/jupyterhub_setup.org` for instructions on how to run the exercises on kubernetes.
