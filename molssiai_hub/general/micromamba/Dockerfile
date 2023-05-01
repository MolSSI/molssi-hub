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

ENV PATH /opt/micromamba/bin:$PATH
ENV MAMBA_EXE /bin/micromamba
ENV MAMBA_ROOT_PREFIX /opt/micromamba

COPY --from=mambaorg/micromamba:1.4.2 /bin/micromamba /bin/micromamba

RUN micromamba shell init --shell=bash --prefix=/opt/micromamba \
 && echo ". /opt/micromamba/etc/profile.d/micromamba.sh" >> /root/.bashrc \
 && echo "micromamba activate base" >> /root/.bashrc \
 && micromamba install -n base python=3.10 \
    -c conda-forge -y \
 && micromamba clean -ay
