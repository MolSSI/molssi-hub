FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV PATH /opt/micromamba/bin:$PATH
ENV MAMBA_EXE /bin/micromamba
ENV MAMBA_ROOT_PREFIX /opt/micromamba

COPY --from=mambaorg/micromamba:1.4.2 /bin/micromamba /bin/micromamba

RUN micromamba shell init --shell=bash --prefix=/opt/micromamba \
 && echo ". /opt/micromamba/etc/profile.d/micromamba.sh" >> /root/.bashrc \
 && echo "micromamba activate base" >> /root/.bashrc \
 && micromamba install -n base python=3.10 \
    -c conda-forge -y \
 && micromamba clean -ay