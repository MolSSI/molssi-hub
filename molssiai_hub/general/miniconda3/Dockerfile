FROM molssiai/debian-bullseye-slim-dev:5.2.2023

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

ENV PATH /opt/conda/bin:$PATH

COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -ay
