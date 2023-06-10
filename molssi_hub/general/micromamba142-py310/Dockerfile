FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV USERNAME molssi
ENV MAMBA_EXE /bin/micromamba
ENV MAMBA_ROOT_PREFIX /home/$USERNAME/micromamba

COPY --from=mambaorg/micromamba:1.4.2 /bin/micromamba ${MAMBA_EXE}

RUN micromamba shell init --shell=bash --prefix=${MAMBA_ROOT_PREFIX} \
 && echo ". ${MAMBA_ROOT_PREFIX}/etc/profile.d/micromamba.sh" >> ~/.bashrc \
 && echo "micromamba activate base" >> ~/.bashrc \
 && micromamba install -n base python=3.10 \
    -c conda-forge -y \
 && micromamba clean -ay