.. _pyscf:

******
PySCF
******

The Python-based Simulations of Chemistry Framework (PySCF) is an open-source 
collection of electronic structure modules written in Python.

Source Specifications
=====================

* **Developers**: `PySCF Developers Team`_ 
* **Github**: https://github.com/pyscf/pyscf
* **Documentation**: https://pyscf.org/user.html

MolSSI-AI Container Hub Specifications
======================================

* **Repository**: https://hub.docker.com/r/chemai/pyscf22-miniconda3-jupyter
* **Tags**: https://hub.docker.com/r/chemai/pyscf22-miniconda3-jupyter/tags
* **Github**: 
* **Dockerfile**: 
* **Image pull command**:

    .. code-block:: bash

        docker pull chemai/pyscf22-miniconda3-jupyter:3.31.2023

* **Container run command**:

    .. code-block:: bash

        docker run \
               -it \
               --name pyscf \
               docker pull chemai/pyscf22-miniconda3-jupyter:3.31.2023 \
               /bin/bash

Image Specifications
^^^^^^^^^^^^^^^^^^^^

* **OS/Arch**: debian:bullseye-slim (linux/amd64)
* **Users**: Root
* **Environment variables**: None
* **Volumes**: None
* **Network**: None
* **Extras**:
    + Added directories: None
    + Important packages installed:

.. citations

.. _PySCF Developers Team: https://pyscf.org/about.html