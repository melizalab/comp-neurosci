
# Computational Neuroscience

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/melizalab/comp-neurosci.git/master)

This repository contains instructional materials for PSYC 5270, a course I teach on computational systems neuroscience at the University of Virginia. Students in this course learn how to process neuroscience data and model the way the brain processes, stores, and generates information. They also gain expertise in using scientific programming (specifically Python and its ecosystem of numerical and graphics libraries) to perform analyses and build models.

The current syllabus is here.

## Getting started

### Cloud

The easiest way to run the exercises is to use [mybinder](https://mybinder.org). This will ensure that you have the latest version of the notebooks, all the data files, and the correct versions of required libraries. Click the badge at the top of this page to start a session. Note that this site does not save your work, so you have to be careful to download your `ipynb` files after you finish a session.

### Local: docker

A [Docker](https://docker.com) image is provided for running the exercises locally. These instructions should work on Windows as well as Linux or OS X.  After installing Docker, run the following commands in your shell (bash for Linux and OS X; PowerShell for Windows):

``` shell
docker pull dmeliza/comp-neurosci:latest
docker run --rm --name comp-neurosci -p 8888:8888 -v "$PWD":/home/jovyan/work dmeliza/comp-neurosci:latest
```

(In PowerShell, replace `"$PWD"` with `${pwd}`. If this is your first time using Docker you may be asked to give permission to access the hard drive and network.)

The last command will start the docker container and the jupyter server. Copy the URL at the bottom of the output into your browser and you should have access to the notebook server. Note: files saved in the `work` subdirectory of the server will appear in your current working directory. Any other files or changes will be lost. Conversely, if you edit a file in the current directory it will show up in the `work` directory.

### Local: OS X and Linux

Install Python 3.5+ and jupyter-notebook with your system package manager.

Debian/Ubuntu: `sudo apt-get install git jupyter-notebook python3-venv`
OS X (with MacPorts): `sudo port install git py36-notebook`

Then clone this directory (`git clone https://github.com/melizalab/comp-neurosci/`), cd into it (`cd comp-neurosci`), and run the following commands to create a virtual environment and link it to your notebook server:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=comp-neurosci
scripts/fetch_data.sh
jupyter-notebook
```

If you're using this option, I recommend working on a copy of the notebook (go to `File/Make a Copy...`. Before each class session, you will need to update your local copy of the repository and then restart the notebook server. From the `comp-neurosci` directory, run the following commands:

``` shell
git pull --rebase
source venv/bin/activate
jupyter-notebook
```

If you get an error on the first command, you probably make changes to one of the notebooks, and git won't overwrite those changes without your permission. Run `git status` to find out which file was changed, make a copy of it, and then run `git stash` to reset your working directory. Then the commands above should work.

### Local: Windows

Install [anaconda](https://www.anaconda.com/distribution/). In anaconda explorer, create a new Python 3.6 environment called `comp-neurosci`. Open a shell in this environment (click `Open Terminal` under the green arrow to the right of the environment), then run the following commands:

``` shell
conda install git numpy scipy pandas matplotlib notebook
git clone https://github.com/melizalab/comp-neurosci
cd comp-neurosci
pip install -r requirements-conda.txt
jupyter-notebook
```

To update your installation as new material is added to the repository, open a terminal in the `comp-neurosci` environment and run the following commands:

``` shell
git pull --rebase
jupyter-notebook
```
