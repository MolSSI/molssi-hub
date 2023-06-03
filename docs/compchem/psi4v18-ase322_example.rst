.. _psi4_ase_example:

*******************
PSI4 + ASE: Example
*******************

Here, we demonstrate the non-interactive usage of the ASE image recipe.

Running ASE with PSI4 Interface Non-interactively
=================================================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **test.inp**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    from ase.calculators.psi4 import Psi4
    from ase.build import molecule
    import numpy as np

    atoms = molecule('H2O')

    calc = Psi4(atoms = atoms,
            method = 'b3lyp',
            memory = '500MB',
            basis = '6-311g_d_p_')

    atoms.calc = calc
    print(atoms.get_potential_energy())
    print(atoms.get_forces())

    calc.psi4.frequency('scf/cc-pvdz', molecule=calc.molecule,
                        return_wfn=True, dertype=1)

This input file creates a PSI4 ASE calculator and stores it in the ASE's ``atoms`` 
object's ``calc`` attribute. The calculator object allows us to interact with PSI4's 
Python API and calculate/fetch molecular properties of interest such as the total 
energy, forces and harmonic vibrational frequencies.

At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── test.inp

Let's copy the docker run command from the 
`catalog <https://molssi-ai.github.io/molssi-ai-hub/compchem/psi4v18-ase322-mamba141-py310.html>`_,
paste it into your terminal and edit it to look like the following command line


.. code-block:: bash

    docker run --rm -v $(pwd):/home molssiai/psi4v18-ase322-mamba141-py310:latest /bin/bash -c "python /home/test.inp"

then press Enter. 

.. note::

    The same Docker image recipe can also be used with Apptainer (Singularity) to
    obtain the same result via the following command

    .. code-block:: bash

        apptainer exec docker://molssiai/ase322-mamba141-py310:latest python test.inp
    
    Note that Apptainer binds ``/home/$USER``, ``/tmp`` and current working directory (``$PWD``)
    from the host system to the running container by default. For further details see the Apptainer 
    `documentation <https://apptainer.org/docs/user/latest/quick_start.html#working-with-files>`_.

If nothing goes wrong, you should see the following lines in your terminal

.. code-block:: bash

    Memory set to 476.837 MiB by Python driver.
    Threads set to 1 by Python driver.
    -2080.2391023908526
    [[-1.88550753e-12  1.76004985e-11 -3.58274965e-01]
     [ 4.19563185e-15 -2.87785885e-01  1.78901243e-01]
     [-1.09633122e-14  2.87785885e-01  1.78901243e-01]]
    Warning: used thermodynamics relations inappropriate for low-frequency modes: ['586.9508' '596.8722' '615.0969']

The first and second line in the output notify us about the program's resource usage.
The third line is the total energy of our system in electron-Volts (eV).
The next three lines within brackets are the elements of our force matrix.
The harmonic vibrational frequencies are shown in the final output line.

.. note::

    You can store the generated output in a separate output file by changing the command as
    follows

    .. code-block:: bash

        docker run --rm -v $(pwd):/home molssiai/psi4v18-ase322-mamba141-py310:latest /bin/bash -c "python /home/test.inp >> /home/test.out"
    
    or

    .. code-block:: bash

        apptainer exec docker://molssiai/psi4v18-ase322-mamba141-py310:latest python test.inp >> test.out

.. caution::

    By default, ASE will store the temporary files for PSI4 in ``/tmp`` within the container filesystem.
    However, because of the ``--rm`` flag in our run command, our container is going to auto-delete itself
    once its work is finished. In order to retain the temporary scratch files that psi4 creates, add the following 
    export bash command to your docker/apptainer run command as shown below


    .. code-block:: bash

        docker run --rm -v $(pwd):/home molssiai/psi4v18-ase322-mamba141-py310:latest /bin/bash -c "export PSI_SCRATCH=/home && python /home/test.inp >> /home/test.out"
    
    or

    .. code-block:: bash

        apptainer exec docker://molssiai/psi4v18-ase322-mamba141-py310:latest sh -c "export PSI_SCRATCH=$PWD && python test.inp >> test.out"

    Since our current working directory on the host machine is binded to ``/home`` within the container,
    the contents of the ``PSI_SCRATCH`` will be retained even after the container is destroyed when the 
    job is finished.