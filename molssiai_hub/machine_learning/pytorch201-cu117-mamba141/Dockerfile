FROM molssiai/mamba141:5.2.2023

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

RUN mamba install pytorch \
    torchvision \
    torchaudio \
    pytorch-cuda=11.7 \
    -c pytorch \
    -c nvidia -yq \
 && mamba clean -ay