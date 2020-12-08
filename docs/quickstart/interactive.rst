Interactive Sessions
====================

Interactive sessions are special jobs which can be started via CLI.

Overview
--------

An interactive session is a job. All options used in running a job can be used. The benefits of an interactive session include:

- backed by docker, i.e. runs seamlessly locally or on the cloud
- azure compute for scaling up and hardware acceleration
- azure compute and `azureml` distribution for scaling out
- completely tracked and auditable
- mount cloud data for read/write

Examples
--------

**Basic**

.. code-block:: console

    % az ml job create --interactive

This will start an interactive bash session locally with the current working directory as an input and ``"azureml/default"`` as the environment. This includes:

- latest stable versions of ``az``, ``git``, and ``gh``
- latest stable versions of all `azureml` interfaces

**Advanced**

.. code-block:: console

    % az ml job create --interactive --target my-cluster --environment azureml/dask --inputs mydata,otherdata --outputs writedata

This will start an interactive bash session locally connected to the remote target ``my-cluster`` with the ``azureml/dask`` environment installed. The ``/mnts/azureml/inputs`` directory will contain the ``mydata`` and ``otherdata`` directories. The ``/mnts/azureml/outputs`` directory will contain the ``writedata`` directory. 

At this point, it may be counterproductive to specify everything on the command line. Instead, we can create a job configuration file ``job.yml``:

.. code-block:: yaml

    name: my-interactive-job
    command: bash
    target: my-cluster
    environment: azureml/dask
    inputs:
      - mydata
      - otherdata
    outputs:
      - writedata
    distribution:
      type: dask
      nodes: 10
      scheduler_class: "dask.distributed.Scheduler"
      worker_class: "dask.distributed.Worker"


Now, start the interactive job, which will now run on 10 nodes:

.. code-block:: console

    % az ml job create --interactive -f job.yml