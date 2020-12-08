Running Jobs
============

Jobs are specifications of a computational unit.

Overview
--------

A job is typically represented as a YAML file.

Hello World
-----------

Write ``job.yml``:

.. code-block:: yaml

    name: my-job
    command: python -c "print('hello world!')"

To run this locally:

.. code-block:: console

    % az ml job create -f job.yml

To run this on ``my-cluster``:

.. code-block:: console

    % az ml job create -f job.yml --target my-cluster

Or alternatively, edit ``job.yml``:

.. code-block:: yaml 

    name: my-job
    command: python -c "print('hello world, from the cloud!')"
    target: my-cluster

Basic
-----


Typically, you want to use an environment with certain data mounted - and *azureml* makes this trivial on local or remote compute.

Write ``job.yml``:

.. code-block:: yaml

    name: my-job
    command: lightgbm --task train --objective multiclass --data $inputs.iris
    target: my-cluster
    environment: azureml/lightgbm
    inputs:
      iris: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv

Now, run the job:

.. code-block:: console

    % az ml job create -f job.yml

This job will execute remotely. To view it in the web UI:

.. code-block:: console 

    % az ml job view --web

To stream the logs:

.. code-block:: console

    % as ml job view --logs --tail 10

Advanced
--------

Advanced stuff.

Workflows
---------

A workflow is simply a job with multiple steps.

Distributed
-----------

See the distribution section.
