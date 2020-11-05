# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.ml import MLClient
from azure.identity import AzureCliCredential
from azure.cli.core.commands.client_factory import get_subscription_id


def ml_environment_create(
        cmd,
        resource_group_name,
        workspace_name,
        environment_name,
        file):
    # TODO : Once EMS supports accepting a version will enable it
    # environment_version=None
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    return ml_client.environments.create_or_update(
        environment_name=environment_name,
        environment_version=None,
        file=file)


def ml_environment_show(
        cmd,
        resource_group_name,
        workspace_name,
        environment_name,
        environment_version=None):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    if environment_version is None:
        return ml_client.environments.get_latest_version(
            environment_name=environment_name
        )
    return ml_client.environments.get(
        environment_name=environment_name,
        environment_version=environment_version)


def ml_environment_list(
        cmd,
        resource_group_name,
        workspace_name):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ml_client = MLClient(subscription_id=subscription_id,
                         resource_group_name=resource_group_name,
                         default_workspace_name=workspace_name,
                         credential=AzureCliCredential())

    return ml_client.environments.list()
