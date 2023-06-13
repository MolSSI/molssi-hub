FROM molssi/debian-bullseye-slim-dev:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

ENV USERNAME molssi
ENV CONDA_ROOT_PREFIX home/${USERNAME}/conda
ENV PATH ${CONDA_ROOT_PREFIX}/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-$(uname -m).sh \
    -O /home/${USERNAME}/miniconda.sh -q \
 && bash /home/${USERNAME}/miniconda.sh -b -p ${CONDA_ROOT_PREFIX} \
 && rm /home/${USERNAME}/miniconda.sh \
 && echo ". ${CONDA_ROOT_PREFIX}/etc/profile.d/conda.sh" >> ~/.bashrc \
 && echo "conda activate base" >> ~/.bashrc \
 && conda clean -afy \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_ROOT_PREFIX} -follow -type f -name '*.js.map' -delete