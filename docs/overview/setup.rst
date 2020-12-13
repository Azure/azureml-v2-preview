Cloud Setup
===========

Azure
-----

If you need an Azure subscription, `create a free account <https://aka.ms/amlfree>`_.

Authentication
~~~~~~~~~~~~~~

Authenticate:

.. code-block:: console

    az login

Configuration
~~~~~~~~~~~~~

If you have access to multiple subscriptions, set a default:

.. code-block:: console

    az account set -s $SUBSCRIPTION_ID

Configure other defaults:

.. code-block:: console

    az config set defaults.workspace="main"
    az config set defaults.location="eastus"
    az config set defaults.group="azureml-rg"

If needed, add your subscription to the allow list:

.. note::
    This is a one-time operation only required during private preview. Onboarding will take around 10 minutes. Once onboarded, running the CURL command will result in a state of "Registered."

.. code-block:: console

    TOKEN=$(`echo "az account get-access-token -s $SUBSCRIPTION_ID -o tsv --query accessToken"`)
    curl --location --request POST "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Features/providers/Microsoft.MachineLearningServices/features/MFE/register?api-version=2015-12-01" --header "Authorization: Bearer $TOKEN" --header 'Content-Length: 0'

Azure Machine Learning
----------------------

Create a Workspace
~~~~~~~~~~~~~~~~~~

Create a workspace:

.. warning::
    Workspace creation from CLI does not work yet, please use the ARM template.

.. image:: https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true
    :target: https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fmldevplatv2.blob.core.windows.net%2Fcli%2Fazuredeploy.json

You're all set! Let's try it out.
