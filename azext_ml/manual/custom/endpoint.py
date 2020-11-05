# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.ml import MLClient
from azure.identity import AzureCliCredential
from azure.cli.core.commands.client_factory import get_subscription_id
ONLINE_ENDPOINT_TYPE = "online"
BATCH_ENDPOINT_TYPE = "batch"


def ml_endpoint_show(cmd,
                     resource_group_name,
                     workspace_name,
                     name,
                     type):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.endpoints.get(type=type, name=name)


def ml_endpoint_create(cmd,
                       name,
                       resource_group_name,
                       workspace_name,
                       system_data=None,
                       description=None,
                       properties=None,
                       traffic_rules=None,
                       compute_configuration=None,
                       auth_mode=None,
                       type=None,
                       file=None,
                       save_as=None):

    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.endpoints.create(type=type, name=name, file=file)


def ml_endpoint_delete(cmd,
                       name,
                       type,
                       resource_group_name,
                       workspace_name):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())
    return ml_client.endpoints.delete(type=type, name=name)
