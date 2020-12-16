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

Verify installation:

.. code-block:: console

    az ml -h

You should see the following output:

.. code-block:: console

    Group
        az ml

    Subgroups:
        code        [Experimental] : Ml code.
        compute     [Experimental] : Ml compute.
        data        [Experimental] : Ml data.
        datastore   [Experimental] : Ml datastore.
        endpoint    [Experimental] : Ml endpoint.
        environment [Experimental] : Ml environment.
        job         [Experimental] : Ml job.
        model       [Experimental] : Ml model.
        workspace   [Experimental] : Ml workspace.
