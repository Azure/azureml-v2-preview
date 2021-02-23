Batch Endpoint (WIP)
====================

Batch Endpoint is used to run batch scoring with a large data input.
Unlike online scoring (also known as realtime scoring) where you get the scoring result right away, batch scoring is executed asynchronously. That is, you trigger a batch scoring job through Batch Endpoint, wait till it is completed, and check later for the scoring results that are stored in your configured output location.

Create a Batch Endpoint
-----------------------

Create a batch endpoint for batch scoring.

.. code-block:: bash
  
  az ml endpoint create --type batch --file examples\endpoints\batch\create-batch-endpoint.yml


Check the batch endpoint details
--------------------------------

Check the details of the batch endpoint along with status. 
You can use the `--query parameter <https://docs.microsoft.com/en-us/cli/azure/query-azure-cli>`_ to get only specific attributes from the returned data.

.. code-block:: bash
  
  az ml endpoint show --name myBatchEndpoint --type batch

Start a batch scoring job
-------------------------

Start a batch scoring job by passing the input data. The input data can be a registered data, cloud path or local path. You will get a job name (a GUID) from the response.
You can also use REST API to start a batch scoring job, see the Appendix below.

.. note:: text
Configurable output is working in progress. Scoring outputs will be stored in your workspace's default blob store now.


Option 1: Input is registered data.

.. code-block:: bash
  
  az ml endpoint invoke --name myBatchEndpoint --type batch --input-data azureml:mnist-data:1


Option 2: Input is cloud path.

.. code-block:: bash
  
  az ml endpoint invoke --name myBatchEndpoint --type batch --input-path https://pipelinedata.blob.core.windows.net/sampledata/mnist

.. code-block:: bash
  
  az ml endpoint invoke --name myBatchEndpoint --type batch --input-datastore <azureml:workspaceblobstore> --input-path data


Option 3: Input is local path.

.. code-block:: bash
  
  az ml endpoint invoke --name myBatchEndpoint --type batch --input-local-path ./batchinput/ --input-datastore <azureml:workspaceblobstore> --input-path bathinput

Check batch scoring job status
------------------------------

Batch scoring job usually takes time to process the entire input. You can monitor the job progress from Azure portal.

1. From your workspace page, click `Studio web URL` to launch studio. 
2. Open `Endpoints` page, click `Pipeline endpoints`.
3. Click endpoint name, and you will see a list of jobs.

or use below command to get the job link.

.. code-block:: bash
  
  az ml job show -n <job-name> --query interaction_endpoints.studio

You can also use below commands to check job status and progress.

Check job detail along with status.

.. code-block:: bash
  
  az ml job show --name <job-name>

Stream job execution log.

.. code-block:: bash
  
  az ml job log --name <job-name>

Get the job name from the invoke response, or use below command to list all jobs. 
By default, jobs under the active deployment (deployment with 100 traffic) will be listed. 
You can also add '--deployment' to get the job lists for a specific deployment.

.. code-block:: bash
  
  az ml endpoint list-jobs --name myBatchEndpoint --type batch

Add a deployment to the batch endpoint
--------------------------------------

One batch endpoint can have multiple deployments hosting different models.

.. code-block:: bash
  
  az ml endpoint update --name myBatchEndpoint --type batch --deployment-file examples\endpoints\batch\add-deployment.yml

Activate the new deployment
---------------------------

Activate the new deployment by switching the traffic (can only be 0 or 100). Now you can invoke a batch scoring job with this new deployment.

.. code-block:: bash
  
  az ml endpoint update --name myBatchEndpoint --type batch --traffic autolog_deployment:100

Appendix: start a batch scoring job using REST clients
------------------------------------------------------

1. Get the scoring URI

.. code-block:: bash
  
  az ml endpoint show --name myBatchEndpoint --type batch --query scoring_uri

2. Get the azure ml access token

Copy the value of the accessToken from the response.

.. code-block:: bash
  
  az account get-access-token

3. Use the scoring URI and the token in your REST client

If you use postman, then go to the Authorization tab in the request and paste the value of the token. Use the scoring uri (please add ?api-version=2020-09-01-preview) from above as the URI for the POST request.