Manage Workspaces
=========

A workspace is a top-level resource for Azure Machine Learning and provides a centralized place to:

- Work with all the artifacts you create during your ML lifecycle such as jobs, models, and endpoints.
- Store a history of all your assets such as training logs, metrics, and snapshots.
- Collaborate with other team members.

Create a workspace
---------------------

To create a workspace with basic configurations:

.. code-block:: console

    az ml workspace create --name <NAME OF WORKSPACE>

Alternatively, you can also create the workspace by defining the parameters in a YAML file:

.. literalinclude:: ../../../examples/workspace/basic-ws-1.yml
   :language: yaml

Then run the following command to create the workspace:

.. code-block:: console

    az ml workspace create --file <YAML FILE PATH>

Workspace specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using a YAML file to define the workspace parameters, it must follow the following schema.

+------------------------+------------------+------------------------------------------------------------------------------------------------------------------------+
| Parameters             | Description                                                                                                                               |
+========================+==================+========================================================================================================================+
| name (required)        | [string] The name of the workspace.                                                                                                       | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| location               | [string] The location to create the workspace in.                                                                                         | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| friendly_name           | [string] An alternative display name.                                                                                                     | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| tags                   | [object] Tags or annotations in the format of `key: value`                                                                                | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| storage_account        | [string] The resource ID of an existing storage account. If not specified, a new one will be created.                                     | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| container_registry     | [string] The resource ID of an existing container registry. If not specified, a new one will be created.                                  | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| key_vault              | [string] The resource ID of an existing key vault. If not specified, a new one will be created.                                           |     
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| app_insights           | [string] The resource ID of an existing application insights. If not specified, a new one will be created.                                | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| hbi_workspace          | [boolean] Whether the customer data is of high business impact (HBI). If not specified, this will be set to false.                        | 
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| private_endpoints      | [object] Private endpoint details. If not specified, users will be allowed to connect to the workspace from any IP addresses.             |
|                        +------------------+------------------------------------------------------------------------------------------------------------------------+
|                        | approval_type    | [enum] The approval type to use on private endpoint connections to the workspace. AutoApproval or ManualApproval.      |
|                        +------------------+------------------------------------------------------------------------------------------------------------------------+
|                        | connections      | [object] One or more connection objects where the key is the `name` and value is an object with the following params:  |
|                        |                  |                                                                                                                        |
|                        |                  |    - subscription_id: The ID of the subscription to create the private endpoint in.                                    |
|                        |                  |    - resource-group: The resource group to create the private endpoint in.                                             |
|                        |                  |    - location: The location to create the private endpoint in. If not specified, the workspace location will be used.  |
|                        |                  |    - vnet_name: Name of the existing virtual network to deploy the private endpoint to.                                |
|                        |                  |    - subnet_name:  Name of the existing subnet to deploy the private endpoint to.                                      |
+------------------------+------------------+------------------------------------------------------------------------------------------------------------------------+
| customer_managed_key   | [object] Key vault details for encrypting data with customer-managed keys. If not specified, Microsoft-managed keys will be used.         |
|                        +------------------+------------------------------------------------------------------------------------------------------------------------+
|                        | key_vault        | [string] The resource ID of the key vault containing the customer managed key.                                         |
|                        +------------------+------------------------------------------------------------------------------------------------------------------------+
|                        | key_uri          | [string] The URI of the customer managed key to use for encrypting data.                                               |
+------------------------+------------------+------------------------------------------------------------------------------------------------------------------------+

Here are a few examples defining different kinds of workspaces.

Basic fields and annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../../../examples/workspace/basic-ws-2.yml
   :language: yaml

Existing associated resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
.. literalinclude:: ../../../examples/workspace/byo-resources-ws.yml
   :language: yaml

Private endpoint connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With a single private endpoint:

.. literalinclude:: ../../../examples/workspace/single-private-endpoint-ws.yml
   :language: yaml

With multiple private endpoints:

.. literalinclude:: ../../../examples/workspace/multiple-private-endpoint-ws.yml
   :language: yaml

Customer-managed keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
.. literalinclude:: ../../../examples/workspace/cmk-ws.yml
   :language: yaml

High business impact (HBI) flag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
.. literalinclude:: ../../../examples/workspace/hbi-ws.yml
    :language: yaml

Update workspace
---------------------
To update a workspace, specify the name of the workspace and a YAML file specifying the new workspace parameters:

.. code-block:: console

    az ml workspace update --name <NAME OF WORKSPACE> --file <YAML FILE PATH>

Show workspace
---------------------
To show the details of an existing workspace:

.. code-block:: console

    az ml workspace show --name <NAME OF WORKSPACE> 

Delete workspace
---------------------
To delete an existing workspace:

.. code-block:: console

    az ml workspace delete --name <NAME OF WORKSPACE> 

List keys in the workspace
---------------------
To list the keys (storage account keys, etc) used in the workspace:

.. code-block:: console

    az ml workspace list-keys --name <NAME OF WORKSPACE> 

Sync keys in the workspace
---------------------
When workspace keys are rotated, you can reset the workspace cache to immediately sync with the new keys. To do this:

.. code-block:: console

    az ml workspace sync-keys --name <NAME OF WORKSPACE> 