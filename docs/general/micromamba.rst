.. _micromamba:

**********
Micromamba
**********

Micromamba is a very compact variant of the mamba package manager.
As a statically linked C++ executable with an independent
command line interface, micromamba does not need a base environment 
to operate and is not distributed with a default version of Python.

Source Specifications
=====================

* **Developers**: `QuantStack & mamba contributors`_
* **Github**: https://github.com/mamba-org/mamba#micromamba
* **Documentation**: https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html

MolSSI-AI Container Hub Specifications
======================================

* **Repository**: https://hub.docker.com/r/chemai/micromamba-py310
* **Tags**: https://hub.docker.com/r/chemai/micromamba-py310/tags
* **Github**: 
* **Dockerfile**: 
* **Image pull command**:

    .. code-block:: bash

        docker pull chemai/micromamba-py310:4.25.2023

* **Container run command**:

    .. code-block:: bash

        docker run \
               -it \
               --name micromamba \
               docker pull chemai/micromamba-py310:4.25.2023 \
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