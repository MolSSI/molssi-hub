FROM molssiai/debian-bullseye-slim-dev:5.2.2023

LABEL maintainer="Mohammad Mostafanejad, \
                  MolSSI-AI, Molecular Sciences Software Institute"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV PATH /opt/conda/bin:$PATH

COPY --from=condaforge/mambaforge /opt/conda /opt/conda

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc \
 && echo "conda activate base" >> /root/.bashrc \
 && conda clean -ay