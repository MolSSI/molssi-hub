.. _torchani:

********
TorchANI
********

TorchANI is a software package based on PyTorch and offers a family 
of (second-generation) ANI neural network potentials. Supported 
potentials include `ANI-1`_, `ANI-1x`_, `ANI-1ccx`_ and `ANI-2x`_.

Source Specifications
=====================

* **Developers**: `Roitberg_Group`_ 
* **Github**: https://github.com/aiqm/torchani
* **Documentation**: https://aiqm.github.io/torchani/index.html

MolSSI-AI Container Hub Specifications
======================================

* **Repository**: https://hub.docker.com/r/chemai/torchani-cu117-miniconda3
* **Tags**: https://hub.docker.com/r/chemai/torchani-cu117-miniconda3/tags
* **Github**: 
* **Dockerfile**: 
* **Image pull command**:

    .. code-block:: bash

        docker pull chemai/torchani-cu117-miniconda3:3.3.2023

* **Container run command**:

    .. code-block:: bash

        docker run \
               -it \
               --name torchani \
               chemai/torchani-cu117-miniconda3:3.3.2023 \
               /bin/bash

.. note::

    For NVIDIA GPU support with nvidia containers, use the following
    container run command

    .. code-block:: bash
        
        docker run \
               -it \
               --name torchani \
               --runtime nvidia \
               --gpus all \
               chemai/torchani-cu117-miniconda3:3.3.2023 \
               bash

    and then run ``nvidia-smi`` to make sure all available GPUs on the docker host
    are visible inside the docker container.

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

.. _ANI-1:    https://www.nature.com/articles/sdata2017193
.. _ANI-1x:   https://aip.scitation.org/doi/abs/10.1063/1.5023802
.. _ANI-1ccx: https://doi.org/10.26434/chemrxiv.6744440.v1
.. _ANI-2x:   https://doi.org/10.26434/chemrxiv.11819268.v1
.. _Roitberg_Group: https://roitberg.chem.ufl.edu