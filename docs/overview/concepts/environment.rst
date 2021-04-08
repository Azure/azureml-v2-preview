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
You can define an environment from an existing Docker image in a publicly accessibly repo by providing the image name.

(Images from private repositories will be supported in an upcoming release).

.. code-block:: console

  az ml environment create --file examples/environments/docker_env.yml


where `docker_env.yml` contains:

.. literalinclude:: ../../../examples/environments/docker_env.yml
   :language: yaml

Create an environment from a Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can also create an environment by providing a custom Dockerfile. Azure ML will build the Docker image from this Dockerfile when the environment is used and the image will be pushed to the workspace's Azure Container Registry.

.. code-block:: console

  az ml environment create --file examples/train/fastai/pets-resnet34/fastai_vision_env.yml

where `fastai_vision_env.yml` contains:

.. literalinclude:: ../../../examples/train/fastai/pets-resnet34/fastai_vision_env.yml
   :language: yaml

Create an environment from a Conda file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Environments can also be created from a Conda specification. The Conda file should adhere to Conda's environment yaml file structure.

Note that you will still need to provide the base Docker image or Dockerfile to use for the environment. If you do not need to provide your own custom image or Dockerfile, you can use one of the official Azure ML Ubuntu Linux-based base images, e.g. "mcr.microsoft.com/openmpi3.1.2-cuda10.2-cudnn8-ubuntu18.04". You can see the full set of supported images in the https://github.com/Azure/AzureML-Containers GitHub repo.

Azure ML will build a Docker image from these specifications, which includes creating a Conda environment with the Conda dependencies specified. Azure ML will execute your job in that Conda environment.

.. code-block:: console

  az ml environment create --file examples/environments/docker_conda_env.yml

Where `conda_env.yml` contains: 

.. literalinclude:: ../../../examples/environments/docker_conda_env.yml
   :language: yaml

where `environment.yml` contains: 

.. literalinclude:: ../../../examples/environments/environment.yml
   :language: yaml

.. note::
  It is required to have the Python interpreter version specified in the Conda specification.


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


Delete an environment
---------------------
.. code-block:: console

  az ml environment delete --name my-data --version 1
