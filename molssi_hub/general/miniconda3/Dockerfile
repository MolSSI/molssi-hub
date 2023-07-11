FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV CONDA_PREFIX /opt/conda
ENV PATH ${CONDA_PREFIX}/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-$(uname -m).sh \
    -O $HOME/miniconda.sh -q \
 && bash $HOME/miniconda.sh -b -p ${CONDA_PREFIX} \
 && rm $HOME/miniconda.sh \
 && echo ". ${CONDA_PREFIX}/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete