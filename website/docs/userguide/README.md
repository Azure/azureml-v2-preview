---
title: Start Here!
slug: /userguide/
---

## Azure ML CLI
```az ml``` is Azure ML on the command line. 
It brings training and scoring capabilities to the terminal next to where you are already working with git and your code.

## Prerequisites
1. An Azure subscription. If you don't have an Azure subscription, [create a free account](https://aka.ms/amlfree) before you begin.
2. A workspace! Don't have one? Use this ARM template!
[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fmldevplatv2.blob.core.windows.net%2Fcli%2Fazuredeploy.json)

## Install the CLI
If you do not have the Azure CLI installed, https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

```
az extension remove -n ml
az extension remove -n azure-cli-ml
az extension add --source https://azuremlsdktestpypi.blob.core.windows.net/wheels/sdk-cli-v2/26401099/ml-0.0.2-py3-none-any.whl --pip-extra-index-urls https://azuremlsdktestpypi.azureedge.net/sdk-cli-v2/26401099 -y
```


## Authentication & CLI setup
```console
az login
az account set -s SUBSCRIPTION_ID
az config set defaults.group=RESOURCE_GROUP
az config set defaults.workspace=WORKSPACE_NAME
```

## Create your first job
Prepare the code you'd like to run. For this example, we'll simply clone the v2 preview repo and run the first example!

```console
git clone https://github.com/Azure/azureml-v2-preview
az ml job create --file azureml-v2-preview/examples/commandjob.yml
```

[Learn more about jobs.](./job)

## Extending the CLI
There are several ways you can make gh your own.

- [az config](https://docs.microsoft.com/en-us/cli/azure/param-persist-howto) set allows you to configure default values used when submitting CLI commands. Examples include workspace and group.
- (more coming soon)

## Feedback
Thank you for checking out Azure ML CLI! Please open an issue to send us feedback. We're looking forward to hearing it.

## Q&A
For Q&A support please visit our [internal StackOverflow](http://aka.ms/stackoverflow)

