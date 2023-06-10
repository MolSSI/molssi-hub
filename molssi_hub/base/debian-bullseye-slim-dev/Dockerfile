FROM debian:bullseye-slim

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Setting the default user
# Change by passing -e USERNAME=XXXX in 'docker run ...'
ARG USERNAME=molssi
ARG USER_UID=1000
ARG USER_GID=$USER_UID

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
        sudo \
# Creating the user
 && groupadd --gid $USER_GID $USERNAME \
 && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
# Adding sudo support. Omit if you don't need to install software after connecting.
 && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Setting the default user. Omit if you want to keep the default as root.
USER $USERNAME