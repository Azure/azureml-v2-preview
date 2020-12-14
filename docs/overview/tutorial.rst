Tutorial
========

Follow this 10 minute tutorial to get started with `azure.ml`.

.. danger::
    This tutorial is not yet functional, please help! Keep it simple.

Hello World!
------------

.. toggle::

    .. warning::
        Local execution is not in scope for private preview.

    Let's start by running our first job tracked in the cloud:

    .. code-block:: console

        az ml job create --command "echo 'hello world!'"

    We can view it in the ML studio:

    .. tip::
        This will open your web browser! Omit the ``--web`` for the CLI view.

    .. code-block:: console 

        az ml job view --web

Hello Azure!
------------

Let's run that on the cloud!

First, create a compute target:

.. code-block:: console

    az ml compute create --name default --vm-size Standard_DS3_v2

Submit to the new compute target:

.. code-block:: console

    az ml job create --command "echo 'hello azure!'" --target default

View the output in the ML studio:

.. code-block:: console

    az ml job view --web

Training a model
----------------

Let's train a simple lightgbm model on the Iris dataset.

.. code-block:: console

    az ml job create --command "lightgbm --task train --objective multiclass --label Species --data $inputs.iris --inputs iris=https://azuremlexamples.blob.core.windows.net/datasets/iris.csv --environment azureml/lightgbm

That's a lot to write out on the command line - let's write it down as ``job.yml``:

.. code-block:: yaml

    command: lightgbm --task train --objective multiclass --label Species --data $inputs.data
    target: default
    environment: azureml/lightgbm
    inputs:
      iris: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv

And run:

.. code-block:: console

    az ml job create -f job.yml

View the run in the studio - check the model artifacts! 

.. code-block:: console

    az ml job view --web

Tune parameters
---------------

Let's add a sweep section to the job configuration to tune the learning rate and [pick something else].

Write ``job-sweep.yml``:

.. code-block:: yaml

    command: >-
        lightgbm --task train 
                 --objective multiclass 
                 --label Species 
                 --learning-rate $inputs.learning_rate 
                 --boosting $inputs.boosting
                 --data $inputs.data
    target: default
    environment: azureml/lightgbm
    inputs:
      iris: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv
    search_space:
      learning-rate:
        spec: uniform
        min_value: 0.001
        max_value: 0.1
      boosting:
        spec: categorical
        options: ["gdbt", "dart"]
    objective:
      primary_metric: accuracy
      goal: maximize

.. code-block:: console

    az ml job create -f job-sweep.yml

Deploy to endpoint
------------------

Let's deploy the best model as an endpoint.

.. code-block:: console 

    az ml endpoint create --name

Let's test the endpoint.

.. code-block:: console 

    az ml endpoint 
    
