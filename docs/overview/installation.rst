Installation
============

You can install *azure.ml* on Linux, MacOS, and Windows for several interfaces.

.. tip::
    Only the command line interface is available for private preview.

Command Line Interface (CLI)
----------------------------

The ``az ml`` CLI provides full access to Azure ML.

Terminal
~~~~~~~~

Launch any terminal. 

.. warning::
    A cloud shell (https://shell.azure.com) is recommended for private preview to avoid conflicting installations.

Azure CLI Install
~~~~~~~~~~~~~~~~~

If you do not have the Azure CLI installed, follow the installation instructions at https://docs.microsoft.com/cli/azure/install-azure-cli.

Verify installation:

.. code-block:: console

    az version

The Azure ML extension requires CLI version **>=2.15.0**. To upgrade your CLI installation, please run the below command.
 
 
.. code-block:: console

    az upgrade

ML Extension Install
~~~~~~~~~~~~~~~~~~~~

Remove any previous extension installations:

.. code-block:: console

    az extension remove -n ml; az extension remove -n azure-cli-ml

Install the Azure CLI extension for ML:

.. tip:: 
    This will be simplified to "``az extension add -n ml``" for public preview.

.. literalinclude:: ../../.github/workflows/runcliwhl.yml
   :lines: 25
   :dedent: 8

Verify installation:

.. code-block:: console

    az ml -h

You should see the following output:

.. code-block:: console

    Group
        az ml
            This command group is experimental and under development. Reference and support levels:
            https://aka.ms/CLI_refstatus
    Subgroups:
        code        : Manage Azure ML code assets.
        compute     : Manage Azure ML compute resources.
        data        : Manage Azure ML data assets.
        datastore   : Manage Azure ML datastores.
        endpoint    : Manage Azure ML endpoints.
        environment : Manage Azure ML environments.
        job         : Manage Azure ML jobs.
        model       : Manage Azure ML models.
        workspace   : Manage Azure ML workspaces.


Python core SDK
----------------------------

The Python core SDK provides functionalities to manage your Azure ML resources, e.g. creating a job for training, deploying an endpoint for inference or listing ML assets.


Install with private index
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

pip install azure-ml -U --extra-index-url https://azuremlsdktestpypi.azureedge.net/sdk-cli-v2