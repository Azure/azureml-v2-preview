# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.ml import MLClient
from azure.identity import AzureCliCredential
from azure.cli.core.commands.client_factory import get_subscription_id


def ml_data_list(cmd,
                 resource_group_name,
                 workspace_name,
                 name):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.data.list(name=name)


def ml_data_show(cmd,
                 resource_group_name,
                 workspace_name,
                 name):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.data.get(name=name)


def ml_data_create(cmd,
                   resource_group_name,
                   workspace_name,
                   name=None,
                   description=None,
                   file=None):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.data.create(name=name, description=description, yaml_path=file)


def ml_data_upload(cmd,
                   resource_group_name,
                   workspace_name,
                   name,
                   path,
                   datastore_name=None,
                   description=None):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    return ml_client.data.upload(name=name, description=description, local_path=path, linked_service_name=datastore_name)


def ml_data_delete(cmd,
                   resource_group_name,
                   workspace_name,
                   name):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.data.delete(name=name)
