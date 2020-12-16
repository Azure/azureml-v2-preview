Manage Models
==============

Models are artifacts generated during a job or uploaded by a user. They contain both the binary artifacts which represent the model as well as instructions on how to use the model to make predictions.

At its simplest, a model is packaged code that takes an input and predicts an output. Creating a machine learning model involves selecting an algorithm and providing it with data. Training is an iterative process that produces a trained model, which encapsulates what the model learned during the training process.	

Create a Model
-----------------

Registered models are identified by name and version. Each time you register a model with the same name as an existing one, the registry assumes that it's a new version. The version is incremented, and the new model is registered under the same name.	Models are identified by name and version. If you register a model with the same name and version as a previously registered model, this will throw an error. You can update the model version or name in the yaml. If you're using MLflow, you can point to the MLmodel file in 

Run the following command to create a model. Note: If you're an MLflow user, you can set the path to the model folder generate in the output of MLflow runs. 

.. code-block:: console

  az ml model create --file azureml-v2-preview/examples/simplemodel.yml


What constitutes a model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Minimum required definition for a model:

.. code-block:: yaml

  name: my-model
  version: 1
  asset_path: ./model
```

Full specification of a model (note: if you're using MLflow this information can be derived from the MLmodel file produced by runs):

.. code-block:: yaml

  name: my-model
  asset_path: ./model
  version: 1
  environment: azureml:AzureML-Minimal/versions/1
  description: this is my test model
  tags:
    foo: bar
    abc: 123
  utc_time_created: '2020-10-19 17:44:02.096572'
  flavors:  # MLflow specific 
    sklearn:
      sklearn_version: 0.19.1
    python_function:
      loader_module: mlflow.sklearn
      python_version: 3.8.5


List models 
--------------
Run the following command to list models in your workspace, use --name paramter to list all models in a workspace with the specified name.

.. code-block:: console

  az ml model list


Show model details
----------

Run the following command to show specific models in your workspace.

.. code-block:: console

  az ml model show --name <model name> --version <version>


Delete models
-------------

Run the following command to delete your model.

.. code-block:: console

  az ml model delete --name <model name> --version <version>


