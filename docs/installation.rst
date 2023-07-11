.. _installation:

*************
Installations
*************

Upon installing Docker or Apptainer on your machine,
you will be able to use any containerized software listed 
in the MolSSI Container Hub. Simply, follow the instructions
below and navigate to the :ref:`quick_start` page for further
instructions on how to unleash the power of containerized
software in your research and hopefully, boost your productivity.

Docker 
======

Users have two options to install Docker on their machines
to be able to use the containerized software in **MolSSI Container Hub**:
`Docker Desktop <https://docs.docker.com/desktop>`_ and 
`Docker Engine <https://docs.docker.com/engine>`_. Docker Desktop is 
the user-friendly option with a nice graphical user interface. It also
comes from multiple Docker packages including Docker Engine. So, if you
choose to install the Docker Desktop on your system, you should not install
the Docker Engine as well. Users who are comfortable interacting with the 
Docker daemon directly through the command-line interface can install Docker
Engine on their system.

Apptainer (Singularity)
=======================

Docker image recipes can also be used with 
`Apptainer <https://apptainer.org/docs/admin/1.1/installation.html>`_. 
Apptainer is an option that comes in handy for non-root users. This is 
a common scenario on supercomputing clusters where users often do not have 
sudo privileges.

Building the Documentation
==========================

The following section is useful for users who want to build the documentation locally
on their machine. If you do not need it, simply skip this section.

.. tip::

    Although not necessary, we recommend building the documentation and its dependencies
    within an isolated ``virtualenv`` or ``conda`` environment. In order to 
    create a ``conda`` environment, run the following command in a terminal
    in the docs folder of this repository

    .. code-block:: bash
        
        conda env create -f requirements.yml

    where, the **requirements.yml** file contains the required dependncies for processing
    the document with *sphinx* and MolSSI theme. The contents of the **requirements.yml**
    is presented in the following block

    .. code-block:: yaml
        
        name: docs 
        channels:
          - defaults
          - conda-forge
        dependencies:
          - numpydoc
          - sphinx-design
          - sphinx-copybutton
          - sphinx
          - pydata-sphinx-theme
          - sphinxcontrib-napoleon
    
    The first line in this yaml file sets the conda environment name to `docs`.
    Should you prefer to choose a different name for your conda environment, 
    simply edit the `name` field in the **requirements.yml** file and run the
    aforementioned `conda create ...` command again. Alternatively, pass
    `-n <env-name>` option to `conda create` to set the environment name on-the-fly.

Now, the conda environment can be activated by running 

    .. code-block:: bash
        
        conda activate <env-name>
    
in a terminal session. The `<env-name>` place-holder should be replaced by the environment
name you chose in a previous step. It is set to `docs` by default.
Once the conda environment is activated run the following command in the **docs** folder of
the main repository

.. code-block:: bash
        
        make html

This command creates the documentation files in the `.html` format in the **docs/_build/html**
directory. The **index.html** file in that directory is your documentation home directory that 
you can open in your browser for further inspection.