.. _contribute:

**********
Contribute
**********

.. contents::
   :local:
   :depth: 2

Naming Convention
=================

Each image recipe will map to a repository on Docker Hub (or any other image registry).
We adopt a simple naming convention for our image recipes which consist of
one mandatory part (shown by ``< >``) and at least three optional parts (indicated by
``[ ]``)

.. code-block:: bash

   <coreSoftwareWWW>-[baseImageXXX]-[baseEnvWWW]-[externalPackagesZZZ]

Here, ``coreSoftware`` is the name of the core software that is conainerized,
and ``baseImage`` refers to the adopted base image that the image recipe will be built
on. 

.. note::

   Use ``baseImage`` when your image recipe is not based on the default base image,
   ``debian-bullseye-slim-dev``. For example, if the first line of your Dockerfile
   does NOT start with
   
   .. code-block:: bash
   
      FROM ``molssi/debian-bullseye-slim-dev``

   you should spacify the name of the base image you use, say, ``ubuntu180``.
   
``baseEnv`` refers to any type of environment that your containerized software
lives in. For example, you may want to install your conteinerized software stack 
within the base conda environment that can be created by ``mamba141``, ``miniconda300`` etc.
 
The ``externalPackages`` denotes the existence of external packages that the core software
might not depend on but they can impact its performance or usage. For example, ASE or PSI4
can be executed from the command line or through Jupyter Notebook interface, if it is present.
Finally, ``WWW``, ``XXX``, ... are the first three digits of the version tag (major, 
minor and patch) according to semantic versioning.

.. note::
   
   Do not include any numerical information from calendar or other customized versioning styles.


Submit Your Recipes
===================

In order to submit your Dockerfiles or Apptainer (Singularity) definition files,
please fork our GitHub repository, create a new folder under the category of your interest
and use the name of your repository on Docker Hub, SingularityHub or other regiestries
(image name without the tag) for this folder. Then, place your Dockerfile or Apptainer 
definition file inside that folder alongside a complete **metadata.json** file which
can be cloned from **molssi_hub/metadata_template.json** template file. Then, 
commit your changes and submit them via a 
`Pull Request <https://github.com/molssi/molssi-hub/pulls>`_.

For example, for submiting images of two containerized quantum chemistry packages
such as PySCF and PSI4, your folder structure should have the following from

.. code-block:: bash

   molssi_hub/
   ├── compchem/
   │   ├── psi4v18-mamba141-py310/
   │   │   ├── Dockerfile
   │   │   └── metadata.json
   │   ├── ...
   │   │   ├── Dockerfile
   │   │   └── metadata.json

That is, **psi4v18-mamba141-py310** is a subfolder of **compchem** category 
and will have its own **Dockerfile** and **metadata.json** files. If everything is
sorted properly, our CI workflow will pickup the information stored in the metadata
JSON files and process them into templated 
`catalog pages <https://molssi.github.io/molssi-hub>`_.

We will review your PR and respond to your request as soon as possible.

Report Bugs
===========

Open a new `issue <https://github.com/molssi/molssi-hub/issues>`_ to report a bug.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.