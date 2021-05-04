
## Get set up

1. Create a workspace.


1. Install the CLI:
   (find install instructions)
   
1. Set some defaults:
  - az account set -s \<my-subscription-id>
  - az configure --defaults group=\<my-resource-group>
  - az configure --defaults workspace=\<my-workspace>
  -  Optional: To change the default output format to yaml, run `az configure` and use the interactive guide.

## Try out command job

1. Create a command job inline (no YML)
Figure out the fields required to create the job.

1. Create a CommandJob from a YML file

1. Create a data asset

  `az ml data upload --name <data-asset-name>:<version> --path ..\python\sample1.csv`

1. Show the data asset you created

  `az ml data show --name <data-asset-name>:<version>`

1. Create a command job with a custom image

1. Stream the logs for your new job: `az ml job stream --name <my-job-name>`

1. View the job in the Studio: `az ml job show --name <my-job-name>` and find the Studio URL (under Properties->interactionEndpoints).

1. Download the job logs to your current directory: `az ml job download --name <my-job-name>`.

You can also list your jobs with `az ml job list`.

## Create a SweepJob

Open sweep_from_command_job.yaml. Update the environment, input, compute cluster, name, and experiment name. Then submit your sweep job: `az ml job create --file sweep_from_command_job.yaml`.

You can view the job in the Studio to see its child runs.

## Create a registered model

First, create a registered model. We'll use a model I've already downloaded for this tutorial. Open model.yml and update the environment. You must also provide a model name and model version. Then create the model asset with `az ml model create --file model.yml`. You can also *list* and *show* models.

## Deploy a model

Try deploying a model you registered.
