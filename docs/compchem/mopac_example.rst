.. _mopac_example:

**************
MOPAC: Example
**************

Here, we demonstrate the non-interactive usage of the MOPAC image recipe.

Running MOPAC Non-interactively
===============================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **test.mop**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    AM1 1SCF
    Formic acid
    Example of a single-point calculation
    O
    C    1.20 1
    O    1.32 1  116.8 1    0.0 0   2  1
    H    0.98 1  123.9 1    0.0 0   3  2  1
    H    1.11 1  127.3 1  180.0 0   2  1  3
    0    0.00 0    0.0 0    0.0 0   0  0  0

This input file drives a single-point self-consistent field (SCF) 
calculation on formic acid using AM1 semi-empirical model.

.. note::

    Using the keyword ``1SCF`` is the  
    `recommended way <http://openmopac.net/manual/example_1SCF.html>`_ to perform a 
    single-point SCF energy calculation in MOPAC.

At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── test.mop

It's time to copy the docker run command from the 
`catalog <https://molssi.github.io/molssi-hub/compchem/mopac220-mamba141.html>`_,
paste it into your terminal and edit it to look like the following command line


.. code-block:: bash

    docker run --rm -w /home/molssi/temp -v $(pwd):/home/molssi/temp molssi/mopac220-mamba141:latest /bin/bash -c "mopac test.mop test.out"

then press Enter. 

.. note::

    The same Docker image recipe can also be used with Apptainer (Singularity) to
    obtain the same result via the following command

    .. code-block:: bash

        apptainer exec docker://molssi/mopac220-mamba141:latest mopac test.mop test.out
    
    Note that Apptainer binds ``/home/$USER``, ``/tmp`` and current working directory (``$PWD``)
    from the host system to the running container by default. For further details see the Apptainer 
    `documentation <https://apptainer.org/docs/user/latest/quick_start.html#working-with-files>`_.

.. caution::

    Ignore (usually many) wanings that you might get the first time a SIF file is being created.
    This is because of Apptainer's `fakeroot <https://apptainer.org/docs/user/1.1/fakeroot.html>`_ 
    feature which allows an unprivileged user to run containers as root by default.

If nothing goes wrong, you should see the following lines in your terminal

.. code-block:: bash

    MOPAC Job: "test.mop" ended normally on Jun  1, 2023, at 18:19.

Your directory should now have the following structure

.. code-block::

    temp/
    ├── test.mop
    ├── test.arc
    └── test.out

.. note::

    If you're a pessimist, run the following command to see if the job has finished normally

    .. code-block:: bash

        grep "JOB ENDED" test.out
    
    You should see the following output in your terminal

    .. code-block:: bash

        * JOB ENDED NORMALLY *