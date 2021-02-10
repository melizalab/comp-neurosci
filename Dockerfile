FROM jupyter/scipy-notebook:a0a544e6dc6e

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN conda install rise --no-deps --yes
RUN conda install -c conda-forge brian2
COPY requirements-conda.txt ./
RUN pip install -r requirements-conda.txt

WORKDIR /home/$NB_USER

ENV datafile comp_neurosci_data_030519.tgz
RUN curl -O https://gracula.psyc.virginia.edu/public/courseware/$datafile \
     && echo "df66410d27ba4d9e234b5a070de28c81bb083892  $datafile" | sha1sum -c - \
     && tar zxvf $datafile \
     && rm $datafile

COPY tools/*.py tools/
COPY images/* images/
COPY --chown=1000 *.ipynb ./
