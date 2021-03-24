Manage Environments
=====================

- Environments are used to define the execution environment of a job or an endpoint.
- All environments are built as docker images.
- We provide convenience functions to generate a environment.

.. note::
  Until July of 2021 any image used for Azure ML training requires Python as an implicit dependency.
  To add python to your own docker image you can run the following: 
  
  RUN apt-get update -qq && \  apt-get install -y python3

Creating an environment
----------------------

Environment can be created in number of ways. For example using docker file, conda file or even a combination of two. This section shows to represent and create environments using YAML files.

Example - Create Environment from YAML file representing the environment.

.. code-block:: console

  az ml environment create --file examples/train/fastai/pets-resnet34/fastai_vision_env.yml


.. literalinclude:: ../../../examples/train/fastai/pets-resnet34/fastai_vision_env.yml
   :language: yaml
   
Environments can be created in number of ways. These examples shows YAML files representing environments for supported scenarios.

Creating Environment using existing Docker Image:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/docker_env.yml


where `fastai-env.yml` contains:

.. literalinclude:: ../../../examples/environments/docker_env.yml
   :language: yaml

Creating Environment using DockerFile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/train/fastai/pets-resnet34/fastai_vision_env.yml

where `fastai_vision_env.yml` contains:

.. literalinclude:: ../../../examples/train/fastai/pets-resnet34/fastai_vision_env.yml
   :language: yaml

Creating Environment using Conda File:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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



Environment Parameters
---------------------

**Required**

- ``name``, type = string

**Optional**

- ``id``, type = guid, defaults to auto-gen on creation 
- ``version``, type = string, default = ``"latest"``
- ``description``, type = string, default = ``""``
- ``tags``, type = map, default = ``{}``
- ``docker_image``, type = string, default = ``"azureml/default"``
- ``docker_file``, type = string, default = ``""``
- ``conda_file``, type = string, default = ``""``
