FROM molssi/mamba141:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

RUN mamba install pytorch=2.0.1 \
    torchvision=0.15.2 \
    torchaudio=2.0.2 \
    pytorch-cuda \
    -c pytorch \
    -c nvidia -yq \
 && mamba clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete