FROM debian:bullseye-slim

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q \
 && apt-get install -q -y --no-install-recommends apt-utils \
    bzip2 \
    ca-certificates \
    git \
    curl \
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

COPY --from=condaforge/mambaforge /opt/conda /opt/conda

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc \
 && echo "conda activate base" >> /root/.bashrc \
 && conda clean -ay
 
