---
title: Start Here!
slug: /userguide/
---

## Azure ML CLI
```az ml``` is Azure ML on the command line. 
It brings training and scoring capabilities to the terminal next to where you are already working with git and your code.

## Prerequisites
1. An Azure subscription. If you don't have an Azure subscription, [create a free account](https://aka.ms/amlfree) before you begin.
2. A workspace! Don't have one? Create a Machine Learning workspace from https://portal.azure.com or use this ARM template.
[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fmldevplatv2.blob.core.windows.net%2Fcli%2Fazuredeploy.json)
3. Onboard your subscription to preview using the onboarding form: http://aka.ms/v2-preview-form 

## Launch a terminal

### Option A - Use the Azure Cloud Shell
You can access the cloud shell at https://shell.azure.com

### Option B - Use your local terminal
You may use any terminal. 
For language server support you can use VSCode :)

If you do not have the Azure CLI installed, follow the installation instructions from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

## Install the Azure ML CLI
Install AzureML CLI extension as follows
```
az extension remove -n azure-cli-ml
az extension add --source https://azuremlsdktestpypi.blob.core.windows.net/wheels/sdk-cli-v2/27359718/ml-0.0.3-py3-none-any.whl --pip-extra-index-urls https://azuremlsdktestpypi.azureedge.net/sdk-cli-v2/27359718 -y
```

## Authentication & CLI setup
NOTE: az login is not required on the cloud shell
```console
az login
az account set -s <SUBSCRIPTION_ID> (GUID)
az config set defaults.group=<RESOURCE_GROUP> (name)
az config set defaults.workspace=<WORKSPACE_NAME> (name)
```

## Create your first job
Prepare the code you'd like to run. For this example, we'll simply clone the v2 preview repo and run the first example!

```console
git clone https://github.com/Azure/azureml-v2-preview
```

**NOTE: To authenticate the git clone, you may need a PAT. You can generate one here: https://github.com/settings/tokens (use anything as username, the PAT as your password)**

Check that a compute cluster exists in your workspace and the name (goazurego) matches the one specified in the https://github.com/Azure/azureml-v2-preview/examples/commandjob.yml file. If you used the ARM template, this will be set up for you. Submit your first job using the job create command. You should see a new run from the Studio UI (https://ml.azure.com) Home page or Experiments page. 

```console
az ml job create --file azureml-v2-preview/examples/train/basic-command-job/pip_freeze_job.yml
```

[Learn more about jobs.](./job)

## Understanding commandjob.yml and az ml job create
A few interesting things to note about the yaml file:

```console
name: test1
compute:
  target: azureml:goazurego
command: /bin/sh -c 'pip freeze && echo hello world'
environment: azureml:AzureML-Minimal:1
code:
  directory: .
```

- 'name' is the user defined run name which needs to be **unique**. By default, runs are created in an Experiment called "Default". If you want to use a different experiment name, you can use the parameter experiment_name.
- 'name' and other parameters can be overwritten from the command line. For example: az ml job create --file azureml-v2-preview/examples/commandjob.yml --name test2
- 'directory' path is relative to where the yaml file exists, not where the command is being run from.
- All the files from 'directory' are uploaded as snapshot before the job is created and can be viewed in the Snapshot page of the run from Studio UI.
- 'azureml' is a special moniker used to refer to an existing entity within the workspace. In this case 'azureml:AzureML-Minimal:1' is expecting that version 1 of an environment called AzureML-Minimal exists in the current workspace. Similarly, 'azureml:testCompute' refers to a compute cluster called 'testCompute' in the current workspace. 
- 'command' parameter refers to the command that gets run on the remote compute. This usually gets replaced by the relevant training command, example: "python train.py" or "Rscript train.R".

## Useful CLI commands
- ```--name pipfreeze_$GITHUB_RUN_ID ```
- ```--query metadata.interaction_endpoints.studio```

## Extending the CLI
There are several ways you can make gh your own.

- [az config](https://docs.microsoft.com/en-us/cli/azure/param-persist-howto) set allows you to configure default values used when submitting CLI commands. Examples include workspace and group.
- (more coming soon)

## Feedback
Thank you for checking out Azure ML CLI! Please open an issue at https://github.com/Azure/azureml-v2-preview/issues to send us feedback. We're looking forward to hearing it.

## Q&A
For Q&A support please visit our [internal StackOverflow](http://aka.ms/stackoverflow) with tag `azure-machine-learning`. GitHub and LinkedIn employees can obtain access by following the guidelines [here](https://www.1eswiki.com/wiki/Stack_Overflow_At_Microsoft_Access) under "Edge Cases".

## Whitelist your subscription (if not whitelisted)
Run the following commands in the cloudshell to whitelist your subscription.

```console
SUBSCRIPTION=`az account show -o tsv --query id`
TOKEN=$(`echo "az account get-access-token -s $SUBSCRIPTION -o tsv --query accessToken"`)
curl --location --request POST "https://management.azure.com/subscriptions/$SUBSCRIPTION/providers/Microsoft.Features/providers/Microsoft.MachineLearningServices/features/MFE/register?api-version=2015-12-01" --header "Authorization: Bearer $TOKEN" --header 'Content-Length: 0'
```

