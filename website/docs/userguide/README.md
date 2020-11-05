---
title: README
slug: /userguide/
---

Welcome to the AML User Guide!

# Install the CLI
We have pre-built the Azure ML CLI as part of this Git repository. Simply run the following commands to set up your CLI environment

```bash
wget https://github.com/Azure/azureml-v2-preview/suites/1447370079/artifacts/24618504
tar xvf {cli.zip} -C ./azureml2/cli
set AZURE_EXTENSION_DIR=path/you/downloaded/to
az ml -h
```

This should show off the new set of AZ CLI commands and you'll be all set to get started.


## Get set up

1. Create a workspace in _Vienna Personal 1_ subscription, in the master region.

1. Install the CLI:

   Open a new PowerShell terminal (or open VS Code and launch a PowerShell terminal)
   Create a new conda environment and activate it
   Install (npm)[https://www.npmjs.com/] if it is not installed.
   Install the (autorest npm package)[https://www.npmjs.com/package/autorest]: *npm install -g autorest*.
   Run *git clone https://msdata.visualstudio.com/Vienna/_git/sdk-cli-v2*
   *cd sdk-cli-v2*
   *python scripts\dev_setup.py -s*
   *python scripts\dev_setup.py -c*
   The script will print out a command to set an environment variable. Run that in your PowerShell terminal.

1. Set some defaults:
  az account set -s <my-subscription-id>
  az configure --defaults group=<my-resource-group>
  az configure --defaults workspace=<my-workspace>
  
  Optional: To change the default output format to yaml, run `az configure` and use the interactive guide. I haven't found another way to change this setting.

1. In your PowerShell window, go to the directory *sdk-cli-v2\samples\yaml*.

## Create a CommandJob

Run the commands below to create a command job. Most commands take a yaml file as input. *You must edit each file before submitting it*. The directions walk you through the process of editing the first file.

1 Create a data asset

  You should create a data asset for your command job to consume. You must provide a name and version, like "newdata:1". 

  `az ml data upload --name <data-asset-name>:<version> --path ..\python\sample1.csv`

  and show the dataset you just created:

  `az ml data show --name <data-asset-name>:<version>`

1. Create a command job

  Open code_job.yaml and make several changes:

   1. Set the job name. Each job must have a unique name in your workspace.
   1. Update the environment string: set the subscription ID, resource group, workspace name, and environment name. The version string is required.
   1. Update the input string: set the subscription ID, resource group, workspace name, and data asset name, and version.
   1. Set the name of your compute cluster. You can list the computes in your workspace with `az ml compute list`.

1. Submit the job: `az ml job create --file code_job.yml`.

1. Stream the logs for your new job: `az ml job stream --name <my-job-name>`

1. View the job in the Studio: `az ml job show --name <my-job-name>` and find the Studio URL (under Properties->interactionEndpoints).

1. Download the job logs to your current directory: `az ml job download --name <my-job-name>`.

You can also list your jobs.

## Create a SweepJob

Open sweep_from_command_job.yaml. Update the environment, input, compute cluster, name, and experiment name. Then submit your sweep job: `az ml job create --file sweep_from_command_job.yaml`.

You can view the job in the Studio to see its child runs.

## Create an endpoint

First, create a registered model. We'll use a model I've already downloaded for this tutorial. Open model.yml and update the environment. You must also provide a model name and model version. Then create the model asset with `az ml model create --file model.yml`. You can also *list* and *show* models.

Next, create an endpoint that uses the model. Open endpoint.yaml and update the model and environment. Give the endpoint a name. Set *infrastructure* to the name of an AKS cluster in your workspace. Then deploy the endpoint: `az ml endpoint create --file endpoint.yaml`. You can also *show* and *delete* the endpoint.

## Other things to try

1. Create en environment: `az ml environment create --file environment.yml` (Paul to update the sample)
