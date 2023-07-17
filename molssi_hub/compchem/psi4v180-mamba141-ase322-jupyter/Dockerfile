FROM molssi/psi4v180-mamba141:latest
 
LABEL maintainer="Mohammad Mostafanejad, \
                  Molecular Sciences Software Institute"

COPY --from=molssi/ase322-mamba141:latest ${CONDA_PREFIX} ${CONDA_PREFIX}

RUN mamba install jupyterlab \
    -c conda-forge -yq \
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