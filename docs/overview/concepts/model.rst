Manage Models
==============

Models are artifacts generated during a job or uploaded by a user. They contain both the binary artifacts which represent the model as well as model metadata.

Create a model
--------------

Creating a model registers the model to your workspace under the specified name and version. You can create a model from a local file or directory.
  
Create YAML config file, e.g. model.yml (description and tags are optional):

.. code-block:: yaml

  name: my-model
  version: 1
  description: this is a sample model
  tags:
    foo: bar
  local_path: ./mnist.pt
  
Create the model:

.. code-block:: console

  az ml model create --file model.yml
  
You can also create the model directly using the command options:

.. code-block:: console

  az ml model create --name my-model --version 1 --local-path ./mnist.pt

MLflow models
~~~~~~~~~~~~~
If your model was created via MLflow (mlflow.log_model()), specify the local path to the model folder that contains the model binaries and MLmodel file. 

For example, if the folder containing the MLflow model is named "model":

.. code-block:: console

  az ml model create --name my-model --version 1 --local-path ./model

Show details for a model
------------------------
Show details for the latest version of a model:

.. code-block:: console

  az ml model show --name my-model
  
Show details for a data asset of a specific name and version:

.. code-block:: console

  az ml model show --name my-model --version 1

List models in a workspace
--------------------------
List all models in a workspace:

.. code-block:: console

  az ml model list
  
List all model versions under a specific name:

.. code-block:: console

  az ml model list --name my-model

Delete a model
--------------

.. code-block:: console

  az ml model delete --name my-model --version 1
