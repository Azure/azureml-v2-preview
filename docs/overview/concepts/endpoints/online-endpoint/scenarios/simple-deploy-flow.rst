.. _simple-deploy-flow:

Simple deploy flow
==================

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
    
    az ml endpoint invoke --name my-endpoint --request-file ../../examples/endpoints/online/managed/simple-flow/sample-request.json

Step 3: Check the container logs
--------------------------------

.. code-block:: bash
    
    az ml endpoint log --name my-endpoint --deployment blue --tail 100

by default the logs are pulled from the `inference-server`. However you can pull it from `storage-initializer` container by passing --container `storage-initializer`
