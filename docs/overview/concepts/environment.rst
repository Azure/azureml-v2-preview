Environment
===========

An Environment...

Parameters
----------

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
- ``pip_file``, type = string, default = ``""``

What are Environments?
----------------------

- Environments are used to define the execution environment of a job or an endpoint.
- All environments are built as docker images.
- We provide convenience functions to generate a environment.

Creating an environment
----------------------

Environment can be created in number of ways. For example using docker file, conda file or even a combination of two. This section shows to represent and create environments using YAML files.

Example - Create Environment from YAML file representing the environment.

.. code-block:: console

  az ml environment create --file examples/environments/fastai-vision-env.yml


.. literalinclude:: ../../../examples/environments/fastai-vision-env.yml
   :language: yaml
   
Environments can be created in number of ways. These examples shows YAML files representing environments for supported scenarios.

Creating Environment using existing Docker Image:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/fastai-env.yml


where `fastai-env.yml` contains:

.. literalinclude:: ../../../examples/environments/fastai-env.yml
   :language: yaml

Creating Environment using DockerFile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/fastai-vision-env.yml

where `fastai-vision-env.yml` contains:

.. literalinclude:: ../../../examples/environments/fastai-vision-env.yml
   :language: yaml

Creating Environment using Conda File:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/conda-env.yml

Where `conda-env.yml` contains: 

.. literalinclude:: ../../../examples/environments/conda-env.yml
   :language: yaml

where `environment.yml` contains: 

.. literalinclude:: ../../../examples/environments/environment.yml
   :language: yaml


Creating Environment using DockerFile + Conda File:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  az ml environment create --file examples/environments/docker-conda-env.yml

where `docker-conda-env.yml` contains: 

.. literalinclude:: ../../../examples/environments/docker-conda-env.yml
   :language: yaml
