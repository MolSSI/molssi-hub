FROM molssiai/mamba141:5.2.2023

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

RUN mamba install numpy \
    scipy \
    matplotlib \
    jupyterlab \
    ase \
    pytorch \
    torchvision \
    torchaudio \
    pytorch-cuda=11.7 \
    -c pytorch \
    -c nvidia \
    -c conda-forge -y \
 && pip install torchani==2.2.3 \
 && conda clean -ay