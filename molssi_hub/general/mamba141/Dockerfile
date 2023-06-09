FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV PATH /opt/conda/bin:$PATH

COPY --from=condaforge/mambaforge /opt/conda /opt/conda

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc \
 && echo "conda activate base" >> /root/.bashrc \
 && conda clean -ay