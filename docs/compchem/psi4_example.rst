.. _psi4_example:

*************
PSI4: Example
*************

Here, we show you how to use the PSI4 image non-interactively.


Running PSI4 Non-interactively
==============================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **test.inp**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    molecule benz{
        pubchem:benzene
    }

    set {
       basis     sto-3g
       reference rhf
    }

    energy('scf')

This input file fetches the benzene molecule from the `PubChem <https://pubchem.ncbi.nlm.nih.gov>`_ 
database and performs a simple self-consistent field calculation at the RHF/STO-3G level of theory.
At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── test.inp

It's time to copy the docker run command from the 
`catalog <https://molssi-ai.github.io/molssi-ai-hub/compchem/psi4v18-mamba141-py310.html>`_,
paste it into your terminal and edit it to look like the following command line


.. code-block:: bash

    docker run --rm -v $(pwd):/home molssiai/psi4v18-mamba141-py310:5.23.2023 /bin/bash -c "psi4 /home/test.inp /home/test.out"

then press Enter. If nothing goes wrong, you should see the following lines in your terminal

.. code-block:: bash

    Searching PubChem database for benzene (single best match returned)
    Found 1 result(s)

Your directory should now have the following structure

.. code-block::

    temp/
    ├── test.inp
    ├── test.log
    └── test.out

.. note::

    If you're a pessimist, run the following command to see if the job has finished normally

    .. code-block:: bash

        grep "beer" test.out
    
    You should see the following output in your terminal

    .. code-block:: bash

        *** Psi4 exiting successfully. Buy a developer a beer!
