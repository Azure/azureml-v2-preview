# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def load_environment_params(self):
    with self.argument_context('ml environment create') as c:
        add_common_params(c)
        c.argument('environment_name', options_list=['--name', '-n'], type=str, help="The name under which the environment should be registered")
        c.argument('file', help="The yaml file containing the entity’s AzureML specification.")
        # TODO : Once EMS supports accepting a version will enable it
        # c.argument('version', help="The version id to be set on the version.
        # Any string is allowed, but needs to be unique to the asset,
        # i.e., no two versions of an asset can have the same version.")

    with self.argument_context('ml environment show') as c:
        add_common_params(c)
        c.argument(
            'environment_name',
            options_list=['--name', '-n'],
            type=str,
            help="The name of the environment to retrieve")
        c.argument(
            'environment_version',
            options_list=['--version', '-v'],
            type=str,
            help="The version of the environment to retrieve")

    with self.argument_context('ml environment list') as c:
        add_common_params(c)
