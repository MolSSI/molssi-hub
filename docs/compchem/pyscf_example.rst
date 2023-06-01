.. _pyscf_example:

**************
PySCF: Example
**************

Here, we demonstrate the non-interactive usage of the PySCF image recipe.

Running PySCF Non-interactively
===============================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **test.inp**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    from pyscf import scf, gto

    mol_h2o = gto.M(atom = "O 0 0 0; H 0 1 0; H 0 0 1", basis = "sto-3g")
    rhf_h2o = scf.RHF(mol_h2o)
    e_h2o = rhf_h2o.kernel()

The aforementioned input file performs a single-point energy calculation on water 
molecule at the RHF/STO-3G level of theory.

At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── test.inp

It's time to copy the docker run command from the 
`catalog <https://molssi-ai.github.io/molssi-ai-hub/compchem/pyscf221-base-mamba141-jupyter.html>`_,
paste it into your terminal and edit it to look like the following command line


.. code-block:: bash

    docker run --rm -v $(pwd):/home molssiai/pyscf221-base-mamba141-jupyter:5.15.2023 /bin/bash -c "python /home/test.inp"

then press Enter. 

.. note::

    The same Docker image recipe can also be used with Apptainer (Singularity) to
    obtain the same result via the following command

    .. code-block:: bash

        apptainer exec docker://molssiai/pyscf221-base-mamba141-jupyter:5.15.2023 python test.inp
    
    Note that Apptainer binds ``/home/$USER``, ``/tmp`` and current working directory (``$PWD``)
    from the host system to the running container by default. For further details see the Apptainer 
    `documentation <https://apptainer.org/docs/user/latest/quick_start.html#working-with-files>`_.

Running the aforementioned command should generate the following output in your terminal

.. code-block:: bash

    converged SCF energy = -74.9611711378677

.. note::

    You can store the generated output in a separate output file by changing the command as
    follows

    .. code-block:: bash

        docker run --rm -v $(pwd):/home molssiai/pyscf221-base-mamba141-jupyter:5.15.2023 /bin/bash -c "python /home/test.inp >> /home/test.out"
    
    or

    .. code-block:: bash

        apptainer exec docker://molssiai/pyscf221-base-mamba141-jupyter:5.15.2023 python test.inp >> test.out