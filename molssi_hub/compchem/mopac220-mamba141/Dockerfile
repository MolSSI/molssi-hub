FROM molssi/mamba141:latest
 
LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

RUN mamba install mopac==22.0.6 \
    -c conda-forge -yq \
 && mamba clean -afy \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${MAMBA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete