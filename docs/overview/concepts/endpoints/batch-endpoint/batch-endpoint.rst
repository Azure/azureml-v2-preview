Batch Endpoint (WIP)
====================

Batch Endpoint is used to run batch scoring with a large data input.
Unlike online scoring (also known as realtime scoring) where you get the scoring result right away, batch scoring is executed asynchronously. That is, you trigger a batch scoring job through Batch Endpoint, wait till it is completed, and check later for the scoring results that are stored in your configured output location.

Prerequisite
------------
Batch scoring can't be run locally, so you run them on cloud resources. Run the following command to create a CPU-enabled compute.

.. code-block:: bash
  
  az ml compute create --name cpuCompute --type AmlCompute --min-instances 0 --max-instances 5

Create a Batch Endpoint
-----------------------

Create a batch endpoint for batch scoring.

.. code-block:: bash
  
  az ml endpoint create --type batch --file examples/endpoints/batch/create-batch-endpoint.yml

No-code deployment is supported for MLflow model, that is environment and scoring script will be auto generated. Below is the yaml file. 
To use a registered model, please replace the model section in yaml with **model: azureml:<modelName>:<modelVersion>**.

.. literalinclude:: ../../../../../examples/endpoints/batch/create-batch-endpoint.yml
   :language: yaml

Check the batch endpoint details
--------------------------------

Check the details of the batch endpoint along with status. 
You can use the `--query parameter <https://docs.microsoft.com/en-us/cli/azure/query-azure-cli>`_ to get only specific attributes from the returned data.

.. code-block:: bash
  
  az ml endpoint show --name mybatchendpoint --type batch

Start a batch scoring job
-------------------------

Start a batch scoring job by passing the input data. The input data can be a registered data, cloud path or local path. You will get a job name (a GUID) from the response.
You can also use REST API to start a batch scoring job, see the Appendix below.

**Note**: During private preview, only FileDataset is supported. 

Start a batch scoring job with different input options
``````````````````````````````````````````````````````

Option 1: Input is registered data.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-data azureml:<datasetName>:<datasetVersion>


Option 2: Input is cloud path.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-path https://pipelinedata.blob.core.windows.net/sampledata/nytaxi/taxi-tip-data.csv

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-datastore azureml:workspaceblobstore --input-path taxi-tip-data


Option 3: Input is local path.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-local-path <local-data-path>

Configure output location when start a batch scoring job
````````````````````````````````````````````````````````

Scoring outputs are by default stored in a folder named job id (a GUID) in the workspace's default store. You can configure the output path when invoking.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-path https://pipelinedata.blob.core.windows.net/sampledata/nytaxi/taxi-tip-data.csv --output-datastore azureml:workspaceblobstore --output-path mypath

Overwrite settings when start a batch scoring job
`````````````````````````````````````````````````

Some settings can be overwritten when start a batch scoring job. 
Use ``--mini-batch-size`` to overwrite mini_batch_size if different size of input data is used. 
Use ``--instance-count`` to overwrite instance_count if different compute resource is needed for this job.
Use ``--set`` to overwrite other settings including max_retries, timeout, error_threshold and logging_level.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-path https://pipelinedata.blob.core.windows.net/sampledata/nytaxi/taxi-tip-data.csv --set retry_settings.max_retries=1

Check batch scoring job execution progress
------------------------------------------

Batch scoring job usually takes time to process the entire input. You can monitor the job progress from Azure portal. The portal link is provided in the response of invoke, check `interactionEndpoints.studio`.

You can also get the job link following below:

1. From your workspace page, click `Studio web URL` to launch studio. 
2. Open `Experiments` page, and you will see a list of jobs.

If you prefer using CLI, below are the commands.

Check job detail along with status.

.. code-block:: bash
  
  az ml job show --name <job-name>

Stream job log.

.. code-block:: bash
  
  az ml job stream --name <job-name>

Get the job name from the invoke response, or use below command to list all jobs. Add ``--deployment`` to get the job lists for a specific deployment.

.. code-block:: bash
  
  az ml endpoint list-jobs --name mybatchendpoint --type batch

Check scoring results
---------------------

Follow below steps to view scoring results.

1. Go to the `batchscoring` step's `Outputs + logs` tab, click `Show data outputs`, and click `View output` icon.
2. On the popup panel, copy the path and click `Open Datastore` link.
3. On the bloblstore page, paste above path in the search box. You will find the scoring output in the folder.

Add a deployment to the batch endpoint
--------------------------------------

One batch endpoint can have multiple deployments hosting different models. Use the command below to add a new deployment to an existing batch endpoint.

.. code-block:: bash
  
  az ml endpoint update --name mybatchendpoint --type batch --deployment-file examples/endpoints/batch/add-deployment.yml

This sample uses a non-MLFlow model, you will need to provide environment and scoring script.

.. literalinclude:: ../../../../../examples/endpoints/batch/add-deployment.yml
   :language: yaml

Activate the new deployment
---------------------------

When invoking an endpoint, the deployment with 100 traffic is in use. Use the command below to activate the new deployment by switching the traffic (can only be 0 or 100). Now you can invoke a batch scoring job with this new deployment.

.. code-block:: bash
  
  az ml endpoint update --name mybatchendpoint --type batch --traffic mnist_deployment:100

Use ``endpoint show`` to check which deployment takes 100 traffic, or follow below steps to check in the UI.

1. In Azure Machine Learning studio, go to `Endpoints` page, click `Pipeline endpoints` tab. 
2. Click the endpoint link, click `Published pipelines`.
3. The deployment with 100 traffic has a `Default` tag.

Now you can trigger a batch scoring job using the new deployment.

.. code-block:: bash
  
  az ml endpoint invoke --name mybatchendpoint --type batch --input-path https://pipelinedata.blob.core.windows.net/sampledata/mnist --mini-batch-size 10 --instance-count 2

Appendix: start a batch scoring job using REST clients
------------------------------------------------------

1. Get the scoring URI

.. code-block:: bash
  
  az ml endpoint show --name mybatchendpoint --type batch --query scoring_uri

2. Get the azure ml access token

Copy the value of the accessToken from the response.

.. code-block:: bash
  
  az account get-access-token

3. Use the scoring URI and the token in your REST client

If you use Postman, then go to the Authorization tab in the request and paste the value of the token. Use the scoring uri from above as the URI for the **POST** request.

Option 1: Input is registered data. 

Please provide the full ARMId. Replace with your own information following the sample below. 

.. code-block:: json
  
  {
      "properties": {
          "dataset": {
              "dataInputType": "DatasetId",
              "datasetId": "/subscriptions/{{subscription}}/resourceGroups/{{resourcegroup}}/providers/Microsoft.MachineLearningServices/workspaces/{{workspaceName}}/data/{{datasetName}}/versions/1"
              },
          "outputDataset" : {
            "datastoreId": "/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroup}}/providers/Microsoft.MachineLearningServices/workspaces/{{workspaceName}}/datastores/{{datastorename}}",
            "path": "mypath"
        }        
      }
  }

Option 2: Input is cloud path.

.. code-block:: json
  
  {
      "properties": {
          "dataset": {
            "dataInputType": "DataUrl",
            "Path": "https://pipelinedata.blob.core.windows.net/sampledata/mnist"                  
          }        
      }
  }
