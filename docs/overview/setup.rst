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


**If needed**, add your subscription to the allow list (the following must be executed from a bash terminal):

.. note::
    External users please contact your microsoft account team for onboarding.

    This self registration script is for microsoft tenant (one-time operation per subscription). 
    This will take **around 10 minutes.** Once onboarded, running the CURL command will result in a state of "Registered."

.. code-block:: console

    SUBSCRIPTION_ID=`az account show -o tsv --query id`
    TOKEN=$(`echo "az account get-access-token -s $SUBSCRIPTION_ID -o tsv --query accessToken"`)
    curl --location --request POST "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Features/providers/Microsoft.MachineLearningServices/features/MFE/register?api-version=2015-12-01" --header "Authorization: Bearer $TOKEN" --header 'Content-Length: 0'

Please let us know you are using the private preview by filling out this `onboarding form
<https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR_TNt2p4AONDgvQ7_H0xYN5UNzFTTE5YNkdERUZOSkJQV09NNUszSUsyWS4u>`_.

.. note::
    This is a staged rollout. Current regions available for private preview include canary regions in addition to: **All PROD regions**
    **Managed inference preview** is invite only at this time. The supported regions include westeurope and westus2 (i.e. Azure ML workspace needs to be in these regions)


Azure Machine Learning
----------------------

Create a Workspace
~~~~~~~~~~~~~~~~~~

A workspace is a top-level resource for Azure Machine Learning and provides a centralized place to work with all the artifacts you create during your ML lifecycle. To create a workspace with basic configurations:

.. code-block:: console

    az ml workspace create --name <NAME OF WORKSPACE>

For more advanced workspace configurations, see the following `documentation <concepts/workspace.html>`_.

You're all set! Let's try it out.
