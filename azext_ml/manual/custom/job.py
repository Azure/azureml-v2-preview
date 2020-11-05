# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.ml import MLClient
from azure.identity import AzureCliCredential
from azure.cli.core.commands.client_factory import get_subscription_id


def ml_job_create(cmd,
                  resource_group_name,
                  workspace_name,
                  name=None,
                  code_configuration=None,
                  environment_id=None,
                  data_bindings=None,
                  experiment_name=None,
                  properties=None,
                  tags=None,
                  compute_binding=None,
                  file=None,
                  save_as=None):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    try:
        return ml_client.jobs.submit(job_name=name,
                                     compute_id=compute_binding['compute_id'] if compute_binding is not None else compute_binding,
                                     experiment_name=experiment_name,
                                     environment_id=environment_id,
                                     save_as_name=save_as,
                                     file=file)
    except Exception as err:
        print(str(err))


def ml_job_show(cmd,
                resource_group_name,
                workspace_name,
                name):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    try:
        return ml_client.jobs.get(job_name=name)
    except Exception as err:
        print(str(err))


def ml_job_list(cmd,
                resource_group_name,
                workspace_name):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    try:
        return ml_client.jobs.list()
    except Exception as err:
        print(str(err))


def ml_job_download(cmd,
                    resource_group_name,
                    workspace_name,
                    name,
                    download_path=None):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    try:
        if not download_path:
            download_path = cmd.cli_ctx.local_context.current_dir
        return ml_client.jobs.download_logs(job_name=name, logs_only=True, download_path=download_path)
    except Exception as err:
        print(str(err))


def ml_job_stream(cmd,
                  resource_group_name,
                  workspace_name,
                  name):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    try:
        return ml_client.jobs.stream_logs(job_name=name)
    except Exception as err:
        print(str(err))
