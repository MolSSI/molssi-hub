.. _miniconda3:

***********
Miniconda 3
***********

Miniconda is a free minimal installer for conda and a slim bootstrap 
variant of Anaconda that incorporates conda, Python and their
dependencies alongside a few other useful packages including pip
and zlib.

Source Specifications
=====================

* **Developers**: `Anaconda, Inc`_ 
* **Github**: https://github.com/ContinuumIO/docker-images/tree/master/miniconda3
* **Documentation**: https://docs.conda.io/en/latest/miniconda.html

MolSSI-AI Container Hub Specifications
======================================

* **Repository**: https://hub.docker.com/r/chemai/miniconda3
* **Tags**: https://hub.docker.com/r/chemai/miniconda3/tags
* **Github**: 
* **Dockerfile**: 
* **Image pull command**:

    .. code-block:: bash

        docker pull chemai/miniconda3:4.26.2023

* **Container run command**:

    .. code-block:: bash

        docker run \
               -it \
               --name miniconda3 \
               docker pull chemai/miniconda3:4.26.2023 \
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

.. _Anaconda, Inc: https://www.anaconda.com 