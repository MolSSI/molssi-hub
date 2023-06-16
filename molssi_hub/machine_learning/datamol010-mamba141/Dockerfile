FROM molssi/mamba141:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

RUN mamba install datamol=0.10.3 \
    -c conda-forge -yq \
 && mamba clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete