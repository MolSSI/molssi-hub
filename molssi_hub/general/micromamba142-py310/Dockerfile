FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV MAMBA_EXE /bin/micromamba
ENV MAMBA_ROOT_PREFIX /opt/micromamba
# Added for compatibility with consumer images
ENV CONDA_PREFIX ${MAMBA_ROOT_PREFIX}

COPY --from=mambaorg/micromamba:1.4.2 ${MAMBA_EXE} ${MAMBA_EXE}

RUN micromamba shell init --shell=bash --prefix=${MAMBA_ROOT_PREFIX} \
 && echo ". ${MAMBA_ROOT_PREFIX}/etc/profile.d/micromamba.sh" >> $HOME/.bashrc \
 && echo "micromamba activate base" >> $HOME/.bashrc \
 && micromamba install -n base python=3.10 \
    -c conda-forge -y \
 && micromamba clean -afy \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete
