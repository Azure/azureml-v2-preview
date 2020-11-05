# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.cli.core.commands.parameters import (
    resource_group_name_type
)


def add_common_params(c):
    c.argument('resource_group_name', resource_group_name_type)
    c.argument(
        'workspace_name',
        type=str,
        help='Name of Azure Machine Learning Workspace to use.'
             ' You can configure the default group using `az configure --defaults workspace=<name>`',
        configured_default='workspace')
