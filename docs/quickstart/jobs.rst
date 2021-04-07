Train Models (Create Jobs)
==========================

A Job is a Resource that specifies all aspects of a computation job. It aggregates 3 things:

1. What to run
2. How to run it
3. Where to run it

A user can execute a job via the CLI by executing an `az ml job create` command. The examples below encapsulate how a user might expand their job definition as they progress with their work.



Create your first job
---------------------

For this example, we'll simply clone the v2 preview repo and run the first example!

.. code-block:: bash

    git clone https://github.com/Azure/azureml-v2-preview

Check that a compute cluster exists in your workspace and you have a compute cluster named **goazurego** (if not, you can modify the name of the cluster in your YML file).

.. code-block:: bash

    az ml job create --file azureml-v2-preview/examples/train/basic-command-job/hello_python_job.yml

This will run a simple "hello world" python script. Here is the YML that we ran.

.. literalinclude:: ../../examples/train/basic-command-job/hello_python_job.yml
   :language: yaml

Let's go into more details on the job specification.

Understanding a job specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is a fully fleshed out job specification YML:

.. literalinclude:: ../../examples/iris/iris_job.yml
   :language: yaml

        
``code / directory`` is the path to your code directory relative to where the YML file lives. 

- This directory is uploaded as a snapshot to Azure ML and mounted to your job for execution. 
- All of the files from 'directory' are uploaded as a snapshot before the job is created and can be viewed in the Snapshot page of the run from Studio UI.
     
``command`` defines the command that gets run on the remote compute. 

- ``command`` executes from the root of the code directory defined above.
- This is typically the command, example: ``python train.py`` or ``Rscript train.R`` and can include as many arguments as you desire.

``environment`` defines the docker image virtual environment you want to run your job in.

- ``azureml:`` is a special moniker used to refer to an existing entity within the workspace. 
- ``azureml:AzureML-Minimal:1`` is expecting that version 1 of an environment called AzureML-Minimal exists in the current workspace. 
- You can also specify an environment image inline using the syntax in the hello world example above.

``compute`` defines where you want to run your job and compute-specific information

- ``target`` indicates the compute you want to run your job against. For example, ``azureml:testCompute`` refers to a compute cluster called 'testCompute' in the current workspace.
- You can override the compute (or any parameter) by using ** ``--set compute.target=azureml:cpu-cluster`` **

``inputs`` defines data you want mounted or downloaded for your job.
    
- ``data`` is the reference pointer to the dataset you want to use 
- ``mode`` indicates how you want the data made available in the job. Mount and Download are the two supported options.

``name`` is the (optional) user defined run identifier which needs to be *unique*. If you do not provide a name a GUID name will be generated for you.

- By default, runs are tagged with the experiment name "Default". If you want to use a different experiment name, you can use the parameter *experiment_name.*
- ``--name`` and other parameters can be overwritten from the command line. For example: ``az ml job create --file azureml-v2-preview/examples/commandjob.yml --name test2``

Real training examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's an example that runs  **Python code.**

.. code-block:: bash

    az ml environment create --file examples/train/tensorflow/tf_env.yml
    az ml job create --file examples/train/tensorflow/mnist/tf_mnist_job.yml


.. literalinclude:: ../../examples/train/tensorflow/mnist/tf_mnist_job.yml
   :language: yaml

Here's an example that runs **R code:**

.. code-block:: bash

    az ml job create --file examples/train/r/accident-prediction/r_job.yml

.. literalinclude:: ../../examples/train/r/accident-prediction/r_job.yml
   :language: yaml


Train an XGBoost model
-----------------------

Next, let's train an xgboost model on an IRIS dataset.

Let's navigate to the examples/iris directory in the repository and see what we should do next.

.. code-block:: bash

    cd ./examples/iris/
    
Define your environment
~~~~~~~~~~~~~~~~~~~~~~~~

First we are going to define the xgboost environment we want to run.

.. literalinclude:: ../../examples/iris/xgboost_env.yml
   :language: yaml


.. code-block:: bash

    az ml environment create --file xgboost_env.yml
    
    
Upload data to the cloud
~~~~~~~~~~~~~~~~~~~~~~~~

Next the input data needs to be moved to the cloud -- therefore the user can create a data artifact in the workspace like so:

.. code-block:: bash

    az ml data upload -n irisdata -v 1 --path ./data


The above command uploads the data from the local folder `.data/` to the `workspaceblobstore` (default). It creates a data entity and registers it under the name `irisdata`.

Create your xgboost training job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../../examples/iris/iris_job.yml
   :language: yaml
   
To submit the job:

.. code-block:: console

    az ml job create --file iris_job.yml --name <unique name> --query metadata.interaction_endpoints.studio

The query parameter will return just the studio url for the run, rather than the entire job object. To view the entire job object,
we can use the CLI to show this job:

.. code-block:: bash

    az ml job show <name of previous job>

.. code-block:: yaml

    # yaml-language-server: $schema=https://azuremlsdk2.blob.core.windows.net/latest/commandJob.schema.json
    command: >-
      python train.py 
      --data {inputs.training_data} 
    environment: azureml:xgboost-env:1
    compute:
      target: azureml:<compute-name>
    code: 
      directory: train
    inputs:
      training_data:
        data: azureml:irisdata:1
        mode: mount

The above job can be run without reference to the dataset, by removing the inputs and the arg in the command, since the script sets the default value if no data is input. 
This is to allow further debugging if data store does not work.

.. code-block:: yaml

    # yaml-language-server: $schema=https://azuremlsdk2.blob.core.windows.net/latest/commandJob.schema.json
    command: >-
      python train.py
    environment: azureml:xgboost-env:1
    compute:
      target: azureml:<compute-name>
    code: 
      directory: train
  
Sweep jobs (Hyperparameter Tuning)
----------------------------------

A Sweep job executes a hyperparameter sweep of a specific search space for a job. The below example uses the command job from the previous section as the 'trial' job in the sweep. It sweeps over different learning rates and subsample rates for each child run. The search space parameters will be passed as arguments to the command in the trial job.

.. literalinclude:: ../../examples/iris/iris_sweep.yml
   :language: yaml

This can be executed by running (after setting compute name in yaml):

.. code-block:: console

    az ml job create --file iris_sweep.yml


AutoML jobs (Azure Automated Machine Learning jobs) - PRIVATE PREVIEW state
---------------------------------------------------------------------------

**NOTE: 'AutoML job' (CLI) is currently in PRIVATE PREVIEW.** 
*In order to get access to that PRIVATE PREVIEW for AutoML, please send an email to CESARDL@MICROSOFT.COM requesting access to it.*

Automated Machine Learning, also referred to as Automated ML or AutoML, is the process of automating the time consuming, iterative tasks of machine learning model development. It allows data scientists, analysts, and developers to quickly and easily build ML models with high scale, efficiency, and productivity all while sustaining model quality.

Apply automated ML when you want Azure Machine Learning to train and tune a model for you using the target metric you specify. Automated ML democratizes the machine learning model development process.

Azure AutoML CLI currently supports these three ML tasks:

- Classification (Binary classification and multi-class classification)
- Regression
- Time Series Forecasting

The below example uses the command job similar to previous sections but using a specific .YAML configuration specially made for AutoML jobs. 
The .YAML config below will train multiple models until it finds the best model under the configuration settings (.YAML config file) provided to AutoML.


.. literalinclude:: ../../examples/AutoML/classification/01-portoseguro-classif-job-single-dataset.yaml
   :language: yaml

In order to reference the input dataset, for this PRIVATE PREVIEW only, you need to first upload the dataset into your Azure ML Workspace, then reference to it from the .YAML. In next previews, you will also be able to directly provide a local path to a dataset file and it'll be uploaded automatically to Azure ML.

For the above example, you can download the dataset .csv file from this HTTP URL:

https://azmlworkshopdata.blob.core.windows.net/safedriverdata/porto_seguro_safe_driver_prediction_train.csv


This AutoML job can be executed by running the following CLI command (after setting your compute name in the YAML above):

.. code-block:: console

    az ml job create --file 01-portoseguro-classif-job-single-dataset.yaml


Other Job Types
---------------

Coming soon:

- PipelineJob (s)
