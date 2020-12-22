Train Models (Create Jobs)
============

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

.. note:: To authenticate the git clone, you may need a PAT. You can generate one here: https://github.com/settings/tokens (use anything as username, the PAT as your password)**

Check that a compute cluster exists in your workspace and you have a compute cluster named **goazurego** (if not, you can modify the name of the cluster in your YML file).

.. code-block:: bash

    az ml job create --file azureml-v2-preview/examples/train/basic-command-job/hello_python_job.yml

This will run a simple "hello world" python script. Here is the YML that we ran.

.. literalinclude:: ../../examples/train/basic-command-job/hello_python_job.yml
   :language: yaml

Let's continue by going into more details on the job specification.

Understanding a job specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is a fully fleshed out job specification YML:

.. literalinclude:: ../../examples/iris/iris-job.yml
   :language: yaml

        
``name`` is the user defined run name which needs to be **unique**. **If you do not provide a name a GUID name will be generated for you.**

    - By default, runs are created in an Experiment called "Default". If you want to use a different experiment name, you can use the parameter **experiment_name.** 
    - ``name`` and other parameters can be overwritten from the command line. For example: ```az ml job create --file azureml-v2-preview/examples/commandjob.yml --name test2```

``code / directory`` is the path to your code directory relative to where the YML file lives. 

..    

     - This directory is uploaded as a snapshot to Azure ML and mounted to your job for execution. 
     - All of the files from 'directory' are uploaded as a snapshot before the job is created and can be viewed in the Snapshot page of the run from Studio UI.
     
``command`` parameter refers to the command that gets run on the remote compute. 

..

     - ``command`` executes from the root of the code directory defined above.
     - This is typically the command, example: ``python train.py`` or ``Rscript train.R`` and can include as many arguments as you desire.

``environment`` is a definition or reference of the docker image virtual environment you want to run your job in.

..

     - ``azureml:`` is a special moniker used to refer to an existing entity within the workspace. 
     - ``azureml:AzureML-Minimal:1`` is expecting that version 1 of an environment called AzureML-Minimal exists in the current workspace. 

``compute`` is the definition of where you want to run your job

..

    - ``azureml:testCompute`` refers to a compute cluster called 'testCompute' in the current workspace.
    - You can override the compute (or any parameter) by using ``--set compute.target=azureml:cpu-cluster

``inputs`` is used to define data you want mounted or downloaded into your job.
    
    - ``data`` is the reference pointer to the dataset you want to use 
    - ``mode`` indicates how you want the data made available in the job. Mount and Download are the two supported options.
    
Real training examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's an example that runs  **Python code.**

.. code-block:: bash

    az ml environment create --file examples/environments/tensorflow/tf_env.yml
    az ml job create --file examples/train/tensorflow/mnist/tf_mnist_job.yml


.. literalinclude:: ../../examples/train/tensorflow/mnist/tf_mnist_job.yml
   :language: yaml

Here's an example that runs **R code:**

.. code-block:: bash

    az ml environment create --file examples/train/r/r_cran_env.yml
    az ml job create --file examples/train/r/r_job.yml

.. literalinclude:: ../../examples/train/r/r_job.yml
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

.. literalinclude:: ../../examples/iris/xgboost-env.yml
   :language: yaml


.. code-block:: bash

    az ml environment create --file xgboost-env.yml
    
    
Upload data to the cloud
~~~~~~~~~~~~~~~~~~~~~~~~

Next the input data needs to be moved to the cloud -- therefore the user can create a data artifact in the workspace like so:

.. code-block:: bash

    az ml data upload -n irisdata -v 1 --path ./data


The above command uploads the data from the local folder `.data/` to the `workspaceblobstore` (default). It creates a data entity and registers it under the name `irisdata`.

Create your xgboost training job
~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../../examples/iris/iris-job.yml
   :language: yaml
   
To submit the job:

.. code-block:: console

    az ml job create --file iris-job.yml --name <unique name> --query metadata.interaction_endpoints.studio

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
        mode: Mount

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
  
Sweep Jobs (Hyperparameter Tuning)
----------------------------------

A Sweep job executes a hyperparameter sweep of a specific search space for a job. The below yaml uses the command job from the previous section as the 'trial' job in the sweep. It sweeps over different learning rates and subsample rates for each child run. The search space parameters will be passed as arguments to the command in the trial job.

.. literalinclude:: ../../examples/iris/iris-sweep.yml
   :language: yaml

This can be executed by running (after setting compute name in yaml):

.. code-block:: console

    az ml job create --file iris-sweep.yml


Other Job Types
---------------

Coming soon:

- PipelineJob
- AutoMLJob (s)
