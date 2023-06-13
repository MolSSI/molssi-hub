FROM molssi/mamba141:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV CONDA_ROOT_PREFIX /home/molssi/conda

RUN mamba install pytorch==2.0.1 \
    torchvision=0.15.2 \
    torchaudio=2.0.2 \
    pytorch-cuda=11.7 \
    -c pytorch \
    -c nvidia -yq \
 && mamba clean -afy \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete