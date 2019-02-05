FROM jupyter/scipy-notebook:c7fb6660d096

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

COPY --chown=1000 *.ipynb ./
COPY tools/*.py tools/
COPY images/* images/
COPY data/io-examples/* data/io-examples/
RUN curl -SL https://gracula.psyc.virginia.edu/public/courseware/starling_song_data.tgz \
    | tar -zxv
RUN curl -SL https://gracula.psyc.virginia.edu/public/courseware/zf_cm_intracellular_data.tgz \
    | tar -zxv
