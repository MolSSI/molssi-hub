FROM molssi/mamba141:latest
 
LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

RUN mamba install psi4 \ 
    "pydantic<2.0" \
    -c conda-forge/label/libint_dev \
    -c conda-forge -yq \
 && mamba clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete