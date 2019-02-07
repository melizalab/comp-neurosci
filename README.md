
# Computational Neuroscience

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/melizalab/comp-neurosci.git/master)

This repository contains instructional materials for PSYC 5270, a course I teach on computational systems neuroscience at the University of Virginia. Students in this course learn how to process neuroscience data and model the way the brain processes, stores, and generates information. They also gain expertise in using scientific programming (specifically Python and its ecosystem of numerical and graphics libraries) to perform analyses and build models.

The current syllabus is here.

## Getting started

### Cloud

Click the binder badge above to run the exercises on [mybinder](https://mybinder.org). Note that this site does not save your work, so you have to be careful to download your `ipynb` files after you finish a session.

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

To restart the notebook server (e.g. after rebooting), just run `source venv/bin/activate && jupyter-notebook` from the package directory.

### Local: Windows

Install [anaconda](https://www.anaconda.com/distribution/), then install some required tools through its package manager or by opening the anaconda shell and running `conda install git` and `conda install -c msys m2-bash m2-tar m2-pkg-config m2w64-fftw`

Then clone this directory (`git clone https://github.com/melizalab/comp-neurosci/`), cd into it (`cd comp-neurosci`), and run the following commands in the anaconda shell to create a virtual environment and link it to your notebook server:

``` shell
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name=comp-neurosci
curl -s 'https://gracula.psyc.virginia.edu/public/courseware/starling_song_data.tgz' | tar zxv
jupyter-notebook
```

To restart the notebook server (e.g. after rebooting), just run `source venv/bin/activate && jupyter-notebook` from the package directory.

### Local: docker

[Docker](https://docker.com) is a container management system that lets you run software in a controlled environment. These instructions should work on Windows as well as Linux or OS X. You don't need to download the source of this repository to get this to work. After installing Docker, run the following commands in your shell (bash for Linux and OS X; PowerShell for Windows):

``` shell
docker pull dmeliza/comp-neurosci:latest
docker run --rm --name comp-neurosci -p 8888:8888 -v "$PWD":/home/jovyan/work dmeliza/comp-neurosci:latest
```

(In PowerShell, replace `"$PWD"` with `${pwd}`. If this is your first time using Docker you may be asked to give permission to access the hard drive and network.)

The last command will start the docker container and the jupyter server. Copy the URL at the bottom of the output into your browser and you should have access to the notebook server. Note: files saved in the `work` subdirectory of the server will appear in your current working directory. Any other files or changes will be lost. Conversely, if you edit a file in the current directory it will show up in the `work` directory.
