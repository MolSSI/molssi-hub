FROM molssiai/mamba141:5.2.2023

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

RUN mamba install python=3.10 \
    numpy \
    scipy \
    matplotlib \
    ase==3.22.1 \
    -c conda-forge \
 && conda clean -ay