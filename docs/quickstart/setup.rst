Setup
=====

Azure
-----

If you don't have an Azure subscription, create one for free.

Authenticate with Azure:

.. code-block:: console

    % az login

If you have access to multiple subscriptions, set a default:

.. code-block:: console

    % az account set -s $SUBSCRIPTION_ID

Azure Machine Learning
----------------------

Setup defaults:

.. code-block:: console

    % az config set defaults.group="azureml-rg"
    % az config set defaults.workspace="main"

Create a workspace:

.. code-block:: console

    % az ml workspace create

You're all set! 
