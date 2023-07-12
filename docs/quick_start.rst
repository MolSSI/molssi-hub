.. _quick_start:

***********
Quick Start
***********

.. contents::
   :local:
   :depth: 2

**This page is under development**

.. Tip::
   For using **MolSSI-AI Container Hub**, a basic familiarity 
   with Docker or Apptainer will be helpful but not necessary.
   Make sure you take a glance at the :ref:`installation` page.

   Check the Docker `documentation <https://docs.docker.com/>`_
   if you are unfamiliar with the Docker. The documentation offers
   a nice `tutorial <https://docs.docker.com/get-started/>`_ series
   to get you up and running, quickly.

Structure of MolSSI-AI Container Hub
====================================

The **Molssi Container Hub** provides three ingredients for each
containerized software:

* Image recipie
* Container repository
* Image catalog

Let's focus on a specific software, say, MOPAC to see how the aforementioned
ingredients come into play.

In order to be able to use MOPAC, one normally needs to install it on the host
machine first. This can be done either by building MOPAC from the 
`source repository <https://github.com/openmopac/mopac>`_ or via graphical installer.
One can also use Conda or Fedora package managers or download MOPAC from Google Play Store.
Each route has its complexity and might be suitable for one operating system or another.

One of the benefits of using Docker or Apptainer is that once you have either of them
on your machine, you are set to use any containerized software including those listed
in the **MolSSI Container Hub** without having to install anything else or try figuring
out and meeting their dependencies.


Image Recipes
-------------

For each containerized software, including MOPAC, we provide an 
`image recipe <https://github.com/MolSSI/molssi-hub/blob/main/molssi_hub/compchem/mopac220-mamba141/Dockerfile>`_
which tells you how we build the software inside an isolated environment (container).
For simplicity, think of containers as an entity similar to a portable virtualenv or Conda 
environment and the image recipe similar to an environment YAML file. Since the software is isolated 
in its own filesystem, you can run it on a variety of operating systems in a reproducible manner.

.. tip::

   Once you are comfortable with Docker, you can write your own image recipes or fine-tune those
   available from the **MolSSI Container Hub** towards your needs.


Container Repositories
----------------------

Container repository is a place we build and then *register* our ready-to-use containers on.
Container repository is an entity similar to `PyPI <https://pypi.org/>`_ which is a 
repository for software written in Python: you can search through the repository, find your
software and fetch it into your system to use using a command such as `pip install ...`. 
There can be a variety of container repositories within a container registry. 
`Docker Hub <https://hub.docker.com/>`_ is an example of a container registry and the 
one we use it to publish our containerized software. You can use the following command
to fetch the latest version of MOPAC image into your machine

.. code-block:: bash

   docker pull molssi/mopac220-mamba141:latest

Once you have downloaded the image on your machine, you can use it via the following command

.. code-block:: bash

   docker run --rm -it molssi/mopac220-mamba141:latest /bin/bash

which creates a temporary Docker container and allows you to get access to it through an interactive
PuTTY bash session. Think of this step as running a ``conda activate <env>`` command. You can now
work with your terminal interactively as if you have MOPAC installed on your system. Just run a
``mopac --version`` command to test it.

.. note::

   The ``docker run`` command will use your existing docker image to create the temporary environment
   for you. If the image does not exist on your machine, the ``docker run`` command will fetch the 
   image for you from the repository before running the container. Once you exit from the container
   environment, it is automatically destroyed like it never existed! 

.. tip::

   If you want to retain your environment, you can remove the ``--rm`` flag from your run command.

Image Catalogs
--------------

Image catalogs are auto-generated documentation pages for all information you need about a containerized
software: the developers, the source repository, the links to the container regiestry, image recipes etc.
As an example, you can see in the 
`MOPAC catalog <https://molssi.github.io/molssi-hub/compchem/mopac220-mamba141.html>`_ that we have also 
included the Docker commands that you will need to pull/run the containers from their repository.

Thus, when you want to use any containerized software listed on the **MolSSI Container Hub**, the fastest 
way might be to just go to the `documentation page <https://molssi.github.io/molssi-hub>`_, search for 
your favorite containerized software, nativate to its catalog page and copy-paste the Docker command in 
a terminal to use the software.