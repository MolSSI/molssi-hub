.. _lammps_example:

***************
LAMMPS: Example
***************

Here, we demonstrate the non-interactive usage of the LAMMPS image recipe.

Running LAMMPS Non-interactively
================================

First, let's create a temporary folder, ``temp`` in your **home** directory
and ``cd`` to it

.. code-block:: bash

    mkdir ~/temp && cd ~/temp

Use your favorite text editor to create a new input file. Let's call it **in.lj**
and copy-paste the following code block into it and then, save it.

.. code-block:: python

    # 1) Initialization
    units lj
    dimension 3
    atom_style atomic
    pair_style lj/cut 2.5
    boundary p p p

    # 2) System definition
    region simulation_box block -20 20 -20 20 -20 20
    create_box 2 simulation_box
    create_atoms 1 random 1500 341341 simulation_box
    create_atoms 2 random 100 127569 simulation_box

    # 3) Simulation settings
    mass 1 1
    mass 2 1
    pair_coeff 1 1 1.0 1.0
    pair_coeff 2 2 0.5 3.0

    # 4) Visualization
    thermo 10

    # 5) Run
    minimize 1.0e-4 1.0e-6 1000 10000

This input file is borrowed from LAMMPS Tutorial 
`page <https://lammpstutorials.github.io/sphinx/build/html/tutorials/lennardjones.html#the-input-script>`_
and intends to run a molecular dynamics simulation of a Lennard-Jones
binary fluid consisting of neutral dots with Langevin thermostat within the NVT ensemble.

At this stage, the content of your directory should look like the following

.. code-block:: bash

    temp
    └── in.lj

Let's copy the docker run command from the `catalog <https://molssi.github.io/molssi-hub/compchem/lammps-mamba141.html>`_,
paste it into a terminal and edit it to look like the following command line

.. code-block:: bash

    docker run --rm -w /home -v $(pwd):/home molssi/lammps-mamba141:latest /bin/bash -c "lmp_serial -in in.lj"

then press Enter. If nothing goes wrong, you should see a long list of lines ending in

.. code-block:: bash

    Nlocal:           1600 ave        1600 max        1600 min
    Histogram: 1 0 0 0 0 0 0 0 0 0
    Nghost:            756 ave         756 max         756 min
    Histogram: 1 0 0 0 0 0 0 0 0 0
    Neighs:           2178 ave        2178 max        2178 min
    Histogram: 1 0 0 0 0 0 0 0 0 0

    Total # of neighbors = 2178
    Ave neighs/atom = 1.36125
    Neighbor list builds = 141
    Dangerous builds = 1
    Total wall time: 0:00:00

.. note::

    The same Docker image recipe can also be used with Apptainer (Singularity) to
    obtain the same result via the following command

    .. code-block:: bash

        apptainer exec docker://molssi/lammps-mamba141:latest lmp_serial -in in.lj
    
    Note that Apptainer binds ``/home/$USER``, ``/tmp`` and current working directory (``$PWD``)
    from the host system to the running container by default. For further details see the Apptainer 
    `documentation <https://apptainer.org/docs/user/latest/quick_start.html#working-with-files>`_.

By default, LAMMPS generates a **log.lammps** file with the auto-generated output upon finishing
the job execution.

.. note::

    You can store the generated output in a separate output file by passing the ``-l <output_name>``
    to the execution command as follows

    .. code-block:: bash

        docker run --rm -w /home -v $(pwd):/home molssi/lammps-mamba141:latest /bin/bash -c "lmp_serial -in in.lj -l log.out"
    
    or

    .. code-block:: bash

        apptainer exec docker://molssi/lammps-mamba141:latest lmp_serial -in in.lj -l log.out