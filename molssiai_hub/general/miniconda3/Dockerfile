FROM debian:bullseye-slim

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q \
 && apt-get install -q -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        mercurial \
        openssh-client \
        procps \
        subversion \
        wget \
        vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV PATH /opt/conda/bin:$PATH

COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -ay
