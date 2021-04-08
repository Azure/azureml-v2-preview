Manage Environments
=====================

Environments are used to define the execution environment of a job or an endpoint and encapsulate the dependencies for training or inference.
All environments are built as Docker images.

.. note::
  Until July of 2021 any image used for Azure ML training requires Python as an implicit dependency.
  To add Python to your own Docker image you can run the following: 
  
  RUN apt-get update -qq && \  apt-get install -y python3

Create an environment
---------------------

Environments can be created in a number of ways. They can be defined from a Docker image, Dockerfile, or Conda specification file. 

The following examples show the different ways to create an environment.

Use the help option for more information on all the valid parameters:

.. code-block:: console

  az ml environment create -h

Create an environment from a Docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/docker_env.yml


where `fastai-env.yml` contains:

.. literalinclude:: ../../../examples/environments/docker_env.yml
   :language: yaml

Create an environment from a Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/train/fastai/pets-resnet34/fastai_vision_env.yml

where `fastai_vision_env.yml` contains:

.. literalinclude:: ../../../examples/train/fastai/pets-resnet34/fastai_vision_env.yml
   :language: yaml

Create an environment from a Conda file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/conda_env.yml

Where `conda_env.yml` contains: 

.. literalinclude:: ../../../examples/environments/conda_env.yml
   :language: yaml

where `environment.yml` contains: 

.. literalinclude:: ../../../examples/environments/environment.yml
   :language: yaml

Note: It is required to have interpreter version specified in the conda specification.

Creating Environment using DockerFile + Conda File:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/docker_conda_env.yml

where `docker_conda_env.yml` contains: 

.. literalinclude:: ../../../examples/environments/docker_conda_env.yml
   :language: yaml


Update an environment
---------------------
See help:

.. code-block:: console

  az ml environment update -h

Show details for an environment
-------------------------------
Show details for the latest version of an environment:

.. code-block:: console

  az ml environment show --name my-env
  
Show details for an environment with a specific name and version:

.. code-block:: console

  az ml environment show --name my-env --version 1

List environments in a workspace
-------------------------------
List all environments in a workspace:

.. code-block:: console

  az ml environment list

List all environment versions under a specific name:

.. code-block:: console

  az ml environment list --name my-env

Delete an environment
---------------------
.. code-block:: console

  az ml environment delete --name my-data --version 1
