FROM debian:bullseye-slim

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q \
 && apt-get install -q -y --no-install-recommends \
        ca-certificates \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        curl \
        openssh-client \
        git \
        procps \
        wget \
        vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*