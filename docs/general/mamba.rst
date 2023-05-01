.. _mamba:

*****
Mamba
*****

Mamba is a fast, robust, and cross-platform package manager.
It supports Windows, OS X and Linux (ARM64 and PPC64LE)
and is compatible with conda packages and covers most conda
commands.

Source Specifications
=====================

* **Developers**: `QuantStack & mamba contributors`_
* **Github**: https://github.com/conda-forge/miniforge-images
* **Documentation**: https://mamba.readthedocs.io/en/latest

ChemHub Specifications
======================

* **Repository**: https://hub.docker.com/r/chemai/mamba
* **Tags**: https://hub.docker.com/r/chemai/mamba/tags
* **Github**: 
* **Dockerfile**: 
* **Image pull command**:

    .. code-block:: bash

        docker pull chemai/mamba:4.26.2023

* **Container run command**:

    .. code-block:: bash

        docker run \
               -it \
               --name mamba \
               docker pull chemai/mamba:4.26.2023 \
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

.. _QuantStack & mamba contributors: https://quantstack.net/index.html