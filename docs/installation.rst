.. _installation:

***********************
Build the Documentation
***********************

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