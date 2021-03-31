Manage Data Assets
====

An Azure ML data asset is a reference to data in your storage, along with metadata. You can use data assets to seamlessly access your data during model training.

When you create a data asset from your local machine, you upload this data into the workspace's default blob storage account (called 'workspaceblobstore').

Create a data asset
-------------------
Data assets can be created from files on your local machine or as references to files in cloud storage. Creating a data asset creates a versioned data asset
that gets registered to your workspace.

The following sections go over the different ways you can create a data asset.

Use the help option for more information on all the valid parameters:

.. code-block:: console

  az ml data create -h

Create a data asset from local files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can create a data asset from files on your local machine. Azure ML will upload this data to the workspace's default datastore (Blob storage account), which
is named 'workspaceblobstore'.

Create YAML config file, e.g. data_from_local.yml:

.. code-block:: yaml

  name: my-data
  version: 1
  local_path: ./mnist

Create data:

.. code-block:: console

  az ml data create --file data_from_local.yml

Create a data asset from a URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can also create a data asset from a storage URL or public URL.

Create YAML config file, e.g. data_from_url.yml:

.. code-block:: yaml

  name: my-data
  version: 1
  path: https://pipelinedata.blob.core.windows.net/sampledata/mnist

Create data:

.. code-block:: console

  az ml data create --file data_from_url.yml

Create a data asset from files in cloud storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create a data asset that references files in cloud storage, specify the datastore and the path to the files on the datastore.

Create YAML config file, e.g. data_from_datastore.yml:

.. code-block:: yaml

  name: my-data
  version: 1
  datastore: azureml:my-datastore
  path: ./mnist

Create data:

.. code-block:: console

  az ml data create --file data_from_datastore.yml


Update a data asset
-------------------
See help:

.. code-block:: console

  az ml data update -h

Show details for a data asset
-----------------------------
Show details for the latest version of a data asset:

.. code-block:: console

  az ml data show --name my-data
  
Show details for a data asset of a specific name and version:

.. code-block:: console

  az ml data show --name my-data --version 1

List data assets in a workspace
-------------------------------
List all data assets in a workspace:

.. code-block:: console

  az ml data list

List all data asset versions under a specific name:

.. code-block:: console

  az ml data list --name my-data

Delete a data asset
-------------------
Delete a data asset. Note that this not delete the underlying data files in your storage service.

.. code-block:: console

  az ml data delete --name my-data

Access data in a job
--------------------
When referencing a data asset in your job configuration, you can either reference a registered data asset (created through ml data create), or you can define the data
inline your job configuration. It is not necessary to explicitly create a data asset in order to access data for a job.
