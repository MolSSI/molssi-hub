.. _rdkitpostgres_example:

********************************
RDKit Postgres Cartridge Example
********************************

This example demonstrates how to use the RDKit cartridge with a PostgreSQL database.
When using the RDKit Postgres container, you can launch the container then access the database server using the `psql` command line tool 
from the host machine or from within the container.

Launching the RDKit Postgres Container
--------------------------------------  

You can launch the server using the following command. 
Note that you should replace `mysecretpassword` with a password of your choice.

.. code-block:: bash

    docker run --name rdkitpostgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d molssi/rdkitpostgres-postgres162:latest


This will start the server. 
You can access it from within the container using the following command.

.. code-block:: bash

    docker exec -it rdkitpostgres psql -U postgres

Because the command set up port mapping (`-p 5432:5432`), you can also access the server from the host machine using the following command.
Note that you will need to have the `psql` command line tool installed on your host machine and enter the password you specified when launching the container.

.. code-block:: bash

    psql -h localhost -U postgres -d postgres


Loading Data
------------

For a more detailed tutorial, please refer to the `RDKit PostgreSQL cartridge documentation <https://www.rdkit.org/docs/Cartridge.html>`_

The following example demonstrates how to load data into the database.

First, make sure the RDKit extension is loaded:

.. code-block:: sql 

    CREATE EXTENSION IF NOT EXISTS rdkit;


Next, create a table called `mols` with a `mol` column.

.. code-block:: sql 

    CREATE TABLE mols (id serial primary key, mol mol);


Next, load a few molecules into the database using SMILES strings:

.. code-block:: sql 

    INSERT INTO mols (mol) VALUES ('c1ccccc1');
    INSERT INTO mols (mol) VALUES ('CCO');
    INSERT INTO mols (mol) VALUES ('CC(=O)O');
    INSERT INTO mols (mol) VALUES ('C(=O)CC');


Querying Data
--------------

You can now perform queries like substring searches, similarity searches, and other analysis associated with RDKit.
For example, to find all molecules that contain a carbonyl group, you can use the following query.

.. code-block:: sql 
    
    SELECT * FROM mols WHERE mol @> 'C(=O)';
  





