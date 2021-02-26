Manage Data Assets
====

Data in Azure ML is used in the context of a Job. 
Data assets can be created from files on your local machine or as references to files in cloud storage.
When you create a data asset from your local machine, you upload this data into the workspace's default blob storage account (called 'workspaceblobstore').


Upload local data
---------------------------

Move some input data to the cloud by creating and naming a data artifact, following the below convention:

.. code-block:: console

  cd azureml-v2-preview/examples/iris/
  az ml data upload -n irisdata -v 1 --path ./data


Create a Data asset from cloud data
-------------------------------------------------------

This example assumes you already have some data in cloud storage.

dataset_from_storage.yml:
.. code-block:: yaml

  name: test_directory_dataset
  version: 1
  datastore: azureml:workspaceblobstore
  directory: v2test


.. code-block:: console
  az ml data create --file dataset_from_storage.yml


Manage Datastore Connections
==========

Datastore connections are used to securely connect to your storage services. Datastores store connection information without putting your authentication credentials and the integrity of your original data source at risk. 

They store connection information, like your subscription ID and token authorization in your Key Vault associated with the workspace, so you can securely access your storage without having to hard code them in your script.

Attach an external datastore
----------------------------

The following command will attach an external storage account to your workspace.
.. code-block:: console

  az ml datastore attach-blob -n anotherstorageaccount SAS_TOKEN

Next, we can create a Data asset which references this other storage account.

dataset_from_another_storage.yml:
.. code-block:: yaml

  name: datafromsomewherelse
  version: 1
  datastore: azure:anotherstorageaccount
  directory: examples/cocodata

.. code-block:: console

  az ml data create --file dataset_from_another_storage.yml

