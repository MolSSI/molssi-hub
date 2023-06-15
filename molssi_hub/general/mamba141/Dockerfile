FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV CONDA_PREFIX /home/molssi/conda
ENV PATH ${CONDA_PREFIX}/bin:$PATH

RUN wget https://github.com/conda-forge/miniforge/releases/download/23.1.0-1/Mambaforge-23.1.0-1-Linux-$(uname -m).sh \
    -O /home/molssi/mambaforge.sh -q \
 && bash /home/molssi/mambaforge.sh -b -p ${CONDA_PREFIX} \
 && rm /home/molssi/mambaforge.sh \
 && echo ". ${CONDA_PREFIX}/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete