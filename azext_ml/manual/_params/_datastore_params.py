# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def load_datastore_params(self):
    with self.argument_context('ml datastore attach-blob') as c:
        add_common_params(c)
        c.argument('account-name', help="name of storage account")
        c.argument('container-name', help="name of blob container to attach to workspace")
        c.argument('name', help="datastore name")
        c.argument('account-key', help="storage account key")
        c.argument('sas-token', help="sas token for storage account")
        c.argument('protocol', help="protocol used to connect to blob container")
        c.argument('endpoint', help="The endpoint of the storage account. Defaults to core.windows.net.")

    with self.argument_context('ml datastore detach') as c:
        add_common_params(c)
        c.argument('name', help="name of datastore to detach from workspace")

    with self.argument_context('ml datastore show') as c:
        add_common_params(c)
        c.argument('include-secrets', action="store_true", help="when argument present, returns secrets for datastore")

    with self.argument_context('ml datastore list') as c:
        add_common_params(c)
        c.argument('include-secrets', action="store_true", help="when argument present, returns secrets for datastore")
