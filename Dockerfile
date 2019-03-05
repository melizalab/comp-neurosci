FROM jupyter/scipy-notebook:83ed2c63671f

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN pip install \
    ewave==1.0.5 \
    libtfr==2.1.2 \
    toelis==2.0.1 \
    quickspikes==1.3.4

RUN conda install rise --no-deps --yes

WORKDIR /home/$NB_USER

ENV datafile comp_neurosci_data_030519.tgz
RUN curl -O https://gracula.psyc.virginia.edu/public/courseware/$datafile \
     && echo "df66410d27ba4d9e234b5a070de28c81bb083892  $datafile" | sha1sum -c - \
     && tar zxvf $datafile \
     && rm $datafile

COPY tools/*.py tools/
COPY images/* images/
COPY --chown=1000 *.ipynb ./
