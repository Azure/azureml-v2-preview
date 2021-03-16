.. _declarative-flow:

Declarative Canary Flow (aka Gitops flow)
=========================================

.. note::
    Private preview for this functionality is invite only at this point

`Canary release <https://martinfowler.com/bliki/CanaryRelease.html>`_ is a deployment approach in which new version of a 
service is introduced to production by rolling out the change to small subset of users/requests before rolling it out 
completely. 

In the example below, we will start by creating a new endpoint with a deployment (v1 of the model, that we call blue).
Then we will scale this deployment to handle more requests. Once we are ready to launch v2 of the model (called green), 
we will do so safely by performing a canary release: Deploy the v2 (i.e. green) but taking no live traffic yet, test
the deployment in isolation, then gradually divert live production traffic (say 10%) to green deployment, and finally,
make the 100% traffic switch to green and delete blue.

What is GitOps
--------------

`GitOps <https://www.atlassian.com/git/tutorials/gitops>`_ is code-based infrastructure and operational procedures that rely on Git as a source control system. It’s an evolution of Infrastructure as Code (IaC) and a DevOps best practice that leverages Git as the **single source of truth, and control mechanism for creating, updating, and deleting system architecture**. More simply, it is the **practice of using Git pull requests to verify and automatically deploy system infrastructure modifications**.

Step 1: Deploy & test the v1 version of the model(blue) in AML Compute 
-----------------------------------------------------------------------

Follow the :ref:`simple-deploy-flow` section to create an endpoint with  "blue" deployment

Step 2: Scale the blue deployment to handle additional traffic
--------------------------------------------------------------
.. code-block:: bash

    az ml endpoint update --name my-endpoint -f examples/endpoints/online/managed/canary-declarative-flow/2-scale-blue.yaml

**Note**: Remember to use same endpoint from simple deployment flow

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-declarative-flow/2-scale-blue.yaml
   :language: yaml

Step 3: Deploy a new model (green) to the endpoint, but taking NO live traffic yet
----------------------------------------------------------------------------------

.. code-block:: bash

    az ml endpoint update --file examples/endpoints/online/managed/canary-declarative-flow/3-create-green.yaml


.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-declarative-flow/3-create-green.yaml
   :language: yaml

**Test the new deployment by directly invoking it** (since invoking the endpoint would only use the blue deployment for now)

.. code-block:: bash

    az ml endpoint invoke --name my-endpoint --deployment green --request-file examples/endpoints/online/model-2/sample-request.json


Step 4: Test the green deployment with a small percentage of the live traffic
-----------------------------------------------------------------------------

.. code-block:: bash

    az ml endpoint update --file examples/endpoints/online/managed/canary-declarative-flow/4-flight-green.yaml

This is the yaml file

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-declarative-flow/4-flight-green.yaml
   :language: yaml

Step 5: Let the green deployment take on the full traffic
---------------------------------------------------------
 
 .. code-block:: bash

    az ml endpoint update --file examples/endpoints/online/managed/canary-declarative-flow/5-full-green.yaml

This is the yaml file

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-declarative-flow/5-full-green.yaml
   :language: yaml

Step 6: Now since green is working fine, lets delete the blue deployment
------------------------------------------------------------------------
 
 .. code-block:: bash

    az ml endpoint update --file examples/endpoints/online/managed/canary-declarative-flow/6-delete-blue.yaml

This is the yaml file

.. literalinclude:: ../../../../../../examples/endpoints/online/managed/canary-declarative-flow/6-delete-blue.yaml
   :language: yaml

Step 7: Cleanup - delete the endpoint
-------------------------------------

.. code-block:: bash

    az ml endpoint delete --name my-endpoint

This deletes the endpoint along with any active deployments