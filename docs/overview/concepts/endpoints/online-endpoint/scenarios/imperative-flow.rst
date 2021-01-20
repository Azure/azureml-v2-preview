.. _imperative-flow:

Imperative Canary Flow
=================================

.. note::
    Private preview for this functionality is invite only at this point

:ref:`declarative-flow` section explains the concept of Canary deployment and how to do it in a fully git backed approach.
In this scenario, we execute a canary deployment flow, however without having to perform all updates via the endpoint yaml.
In this case we will have a yaml file for endpoint and seperate yaml files for each deployment.
Operations like scaling up, changing traffic or deleting deployments can be done directly using the CLI wihtout updating the YAML.
This approach could be useful during development time. The :ref:`declarative-flow` would be useful for a production scenario.

Step 1: Deploy the v1 version of the model(blue) 
-------------------------------------------------

Step 1a: Create an empty endpoint (no deployment and no set traffic rules)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    az ml endpoint create --file examples/endpoints/online/managed/canary-imperative-flow/1-create-endpoint.yaml --wait

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-imperative-flow/1-create-endpoint.yaml
   :language: yaml

Step 1b: create the deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    az ml endpoint update  --name my-new-endpoint --deployment blue --deployment-file examples/endpoints/online/managed/canary-imperative-flow/2-create-blue.yaml --wait

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-imperative-flow/2-create-blue.yaml
   :language: yaml

Step 1c: Set traffic
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    
    az ml endpoint update --name my-new-endpoint --traffic "blue:100" --wait


Step 1d: Test the endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    az ml endpoint invoke --name my-new-endpoint --request-file examples/endpoints/online/model-1/sample-request.json


Step 2: Scale the blue deployment to handle additional traffic
--------------------------------------------------------------

.. code-block:: bash
    
    az ml endpoint update --name my-new-endpoint --deployment blue --instance-count 2 --wait

you can also use the generic --set to update any attribute

.. code-block:: bash
    
    az ml endpoint update --name my-new-endpoint --set deployments.blue.scale.instance_count=2 --wait

Step 3: Deploy a new model (green) to the endpoint, but taking NO live traffic yet
----------------------------------------------------------------------------------

.. code-block:: bash

    az ml endpoint update  --name my-new-endpoint --deployment-file examples/endpoints/online/managed/canary-imperative-flow/3-create-green.yaml --wait

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-imperative-flow/3-create-green.yaml
   :language: yaml

**Test the new deployment by directly invoking it** (since invoking the endpoint would only use the blue deployment for now)

.. code-block:: bash

    az ml endpoint invoke --name my-new-endpoint --deployment green --request-file examples/endpoints/online/model-2/sample-request.json

Step 4: Move small percentage of live traffic to green
------------------------------------------------------

To perform the update directly,

.. code-block:: bash
    
    az ml endpoint update --name my-new-endpoint --traffic "blue:90,green:10" --wait

Step 5: Let the green deployment take on the full traffic
---------------------------------------------------------

.. code-block:: bash
    
    az ml endpoint update --name my-new-endpoint --traffic "blue:0,green:100" --wait

Step 6: Now since green is working fine, lets delete the blue deployment
------------------------------------------------------------------------

.. code-block:: bash
    
    az ml endpoint delete --name my-new-endpoint --deployment blue

Step 7: Cleanup - delete the endpoint
-------------------------------------

.. code-block:: bash
    
    az ml endpoint delete --name my-new-endpoint