.. _ase_example:

************
ASE: Example
************

Here, we demonstrate the non-interactive usage of the ASE image recipe.

Running ASE Non-interactively
=============================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **test.inp**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    from ase import Atoms
    from ase.calculators.emt import EMT

    atom = Atoms('N')
    atom.calc = EMT()
    e_atom = atom.get_potential_energy()

    d = 1.1
    molecule = Atoms('2N', [(0., 0., 0.), (0., 0., d)])
    molecule.calc = EMT()
    e_molecule = molecule.get_potential_energy()

    e_atomization = e_molecule - 2 * e_atom

    print('Nitrogen atom energy: %5.2f eV' % e_atom)
    print('Nitrogen molecule energy: %5.2f eV' % e_molecule)
    print('Atomization energy: %5.2f eV' % -e_atomization)


This input file calculates the atomization energy of nitrogen molecule from
the total energies of isolated nitrogen molecule and nitrogen atom.

At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── test.inp

It's time to copy the docker run command from the 
`catalog <https://molssi.github.io/molssi-hub/compchem/ase322-mamba141.html>`_,
paste it into your terminal and edit it to look like the following command line


.. code-block:: bash

    docker run --rm -w /home -v $PWD:/home molssi/ase322-mamba141:latest /bin/bash -c "python test.inp"

then press Enter. 

.. note::

    The same Docker image recipe can also be used with Apptainer (Singularity) to
    obtain the same result via the following command

    .. code-block:: bash

        apptainer exec docker://molssi/ase322-mamba141:latest python test.inp
    
    Note that Apptainer binds ``/home/$USER``, ``/tmp`` and current working directory (``$PWD``)
    from the host system to the running container by default. For further details see the Apptainer 
    `documentation <https://apptainer.org/docs/user/latest/quick_start.html#working-with-files>`_.

If nothing goes wrong, you should see the following lines in your terminal

.. code-block:: bash

    Nitrogen atom energy:  5.10 eV
    Nitrogen molecule energy:  0.44 eV
    Atomization energy:  9.76 eV

.. note::

    You can store the generated output in a separate output file by changing the command as
    follows

    .. code-block:: bash

        docker run --rm -w /home -v $PWD:/home molssi/ase322-mamba141:latest /bin/bash -c "python test.inp >> test.out"
    
    or

    .. code-block:: bash

        apptainer exec docker://molssi/ase322-mamba141:latest python test.inp >> test.out