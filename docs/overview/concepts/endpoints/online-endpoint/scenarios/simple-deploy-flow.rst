.. _simple-deploy-flow:

Simple deploy flow
==================

.. note::
    Private preview for this functionality is invite only at this point

Step 1: Deploy simple endpoint
------------------------------

.. code-block:: bash 
    
    az ml endpoint create --file examples/endpoints/online/managed/simple-flow/1-create-endpoint-with-blue.yaml --wait

This is the yaml file

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/simple-flow/1-create-endpoint-with-blue.yaml
   :language: yaml

Get the state of endpoint/deployment along with the status
``````````````````````````````````````````````````````````
.. code-block:: bash
    
    az ml endpoint show --name my-endpoint

you can use the `--query parameter <https://docs.microsoft.com/en-us/cli/azure/query-azure-cli>`_ to get only specific attributes from the returned data

Step 2: Now test the endpoint
-----------------------------

.. code-block:: bash
    
    az ml endpoint invoke --name my-endpoint --request-file examples/endpoints/online/model-1/sample-request.json


For instructions on using your own client (like postman) see the Appendix below

Step 3: Check the container logs
--------------------------------

.. code-block:: bash
    
    az ml endpoint log --name my-endpoint --deployment blue --tail 100

by default the logs are pulled from the `inference-server`. However you can pull it from `storage-initializer` container by passing --container `storage-initializer`

Step 4: [Optionally] Delete the endpoint along with the deployment
------------------------------------------------------------------

Do **not** run this step if you plan to run the :ref:`declarative-flow`

.. code-block:: bash

    az ml endpoint delete --name my-endpoint


Appendix
--------

Invoking the scoring endpoint using REST clients
`````````````````````````````````````````````````

**Step 1: Get the scoring URI**

replace 'my-endpoints' with name of your endpoint in the below command

.. code-block:: bash
    
    az ml endpoint show -n my-endpoint --query "scoring_uri"

**Step 2: Get the azure ml auth token**

Copy the value of the accessToken from this

.. code-block:: bash
    
    az ml endpoint list-keys -n my-endpoint

**Step 3: Use the URI and the token in your REST client**

If you use postman, then go to the Authorization tab in the request and paste the value of the token. Use the scoring uri form above as the URI for the POST request.