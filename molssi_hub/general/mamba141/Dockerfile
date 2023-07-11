FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV CONDA_PREFIX /opt/conda
ENV PATH ${CONDA_PREFIX}/bin:$PATH

COPY --from=condaforge/mambaforge ${CONDA_PREFIX} ${CONDA_PREFIX}

RUN echo ". ${CONDA_PREFIX}/etc/profile.d/conda.sh" >> $HOME/.bashrc \
 && echo "conda activate base" >> $HOME/.bashrc \
 && mamba clean -ay \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete