FROM debian:bullseye-slim

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q \
 && apt-get install -q -y --no-install-recommends \
        bzip2 \
        pigz \
        ca-certificates \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        openssh-client \
        git \
        mercurial \
        procps \
        subversion \
        wget \
        vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
