FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV USERNAME molssi
ENV MAMBA_ROOT_PREFIX home/${USERNAME}/conda
ENV PATH ${MAMBA_ROOT_PREFIX}/bin:$PATH

RUN wget https://github.com/conda-forge/miniforge/releases/download/23.1.0-1/Mambaforge-23.1.0-1-Linux-$(uname -m).sh \
    -O /home/${USERNAME}/mambaforge.sh -q \
 && bash /home/${USERNAME}/mambaforge.sh -b -p ${MAMBA_ROOT_PREFIX} \
 && rm /home/${USERNAME}/mambaforge.sh \
 && echo ". ${MAMBA_ROOT_PREFIX}/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -afy \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete