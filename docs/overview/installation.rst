Installation
============

You can install *azure.ml* on Linux, MacOS, and Windows for several interfaces. The CLI is recommended to get started.

CLI
---

The CLI through ``az ml`` provides full access to Azure ML and a set of CLI-specific functionality.

Launch a terminal
~~~~~~~~~~~~~~~~~

You may use any terminal. 

.. tip::
    A cloud shell (https://shell.azure.com) is recommended for private preview.

Install the Azure CLI
~~~~~~~~~~~~~~~~~~~~~

If you do not have the Azure CLI installed, follow the installation instructions at https://docs.microsoft.com/cli/azure/install-azure-cli.

Verify installation:

.. code-block:: console

    az version

Install the ML extension
~~~~~~~~~~~~~~~~~~~~~~~~

Remove any previous extension installations if you have them:

.. code-block:: console

    az extension remove -n ml; az extension remove -n azure-cli-ml

Install the Azure CLI extension for ML:

.. tip:: 
    This will be ``az extension add -n ml`` for public preview.

.. literalinclude:: ../../.github/workflows/runcliwhl.yml
   :lines: 22

Verify installation:

.. code-block:: console

    az ml -h
