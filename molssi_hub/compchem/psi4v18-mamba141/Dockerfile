FROM molssiai/mamba141:5.2.2023
 
LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

RUN mamba install psi4 \
    python=3.10 \
    -c conda-forge/label/libint_dev \
    -c conda-forge \
 && mamba clean -ay