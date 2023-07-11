FROM molssi/pytorch201-cu117-mamba141:latest

LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

RUN mamba install numpy \
    scipy \
    matplotlib \
    ase=3.22.1 \
    jupyterlab \
    -c conda-forge -y \
 && pip install --no-cache-dir torchani==2.2.3 \
 && conda clean -afy \
 && find ${CONDA_PREFIX} -follow -type f -name '*.a' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.pyc' -delete \
 && find ${CONDA_PREFIX} -follow -type f -name '*.js.map' -delete

CMD [ \
     "jupyter", \
     "lab", \
     "--notebook-dir=/home", \
     "--no-browser", \
     "--allow-root", \
     "--ip=*", \
     "--port=8888" \
    ]