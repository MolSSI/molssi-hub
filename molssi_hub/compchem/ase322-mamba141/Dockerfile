FROM molssi/mamba141:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV CONDA_ROOT_PREFIX /home/molssi/conda

RUN mamba install numpy \
    scipy \
    matplotlib \
    ase=3.22.1 \
    -c conda-forge \
 && conda clean -afy \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete