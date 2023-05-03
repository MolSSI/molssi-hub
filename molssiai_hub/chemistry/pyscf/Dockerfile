FROM molssiai/mamba141:5.2.2023
 
RUN pip install pyscf==2.2.1 \
 && mamba install jupyterlab -y \
    -c conda-forge \
 && mamba clean -ay