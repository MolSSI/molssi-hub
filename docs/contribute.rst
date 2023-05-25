.. _contribute:

**********
Contribute
**********

.. contents::
   :local:
   :depth: 2

Submit Your Recipes
===================

In order to submit your Dockerfiles or Apptainer (Singularity) definition files,
please fork our GitHub repository, create a new folder under the category of your interest
and use the name of your repository on Dockerhub, SingularityHub or other regiestries
(image name without the tag) for this folder. Then, place your Dockerfile or Apptainer 
definition file inside that folder alongside a complete **metadata.json** file which
can be cloned from **molssiai_hub/metadata_template.json** template file. Then, 
commit your changes and submit them via a 
`Pull Request <https://github.com/molssi-ai/molssi-ai-hub/pulls>`_.

For example, for submiting images of two containerized quantum chemistry packages
such as PySCF and PSI4, your folder structure should have the following from

.. code-block:: bash

   molssiai_hub/
   ├── compchem/
   │   ├── psi4v18-mamba141-py310/
   │   │   ├── Dockerfile
   │   │   └── metadata.json
   │   ├── pyscf221-base-mamba141-jupyter/
   │   │   ├── Dockerfile
   │   │   └── metadata.json

That is, both folders **psi4v18-mamba141-py310** and **pyscf221-base-mamba141-jupyter**
are subfolders of **compchem** category and will have their own **Dockerfile** and 
**metadata.json** files. If everything is sorted properly, our CI workflow will pickup
the information stored in the metadata JSON files and process them into templated
`catalog pages <https://molssi-ai.github.io/molssi-ai-hub>`_.

We will review your PR and respond to your request as soon as possible.

Report Bugs
===========

Open a new `issue <https://github.com/molssi-ai/molssi-ai-hub/issues>`_ to report a bug.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.