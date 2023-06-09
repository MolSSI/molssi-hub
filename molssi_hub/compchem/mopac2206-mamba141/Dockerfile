FROM molssiai/mamba141:5.2.2023
 
LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

RUN mamba install mopac==22.0.6 \
    -c conda-forge \
 && mamba clean -ay