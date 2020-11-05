# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def load_endpoint_params(self):
    with self.argument_context('ml endpoint create') as c:
        add_common_params(c)
        c.argument('file', help="yaml file to generate code job from")
        c.argument('save_as', help="file to save code job to")
        c.argument('type', help="the type of the endpoint: online or batch")

    with self.argument_context('ml endpoint show') as c:
        add_common_params(c)
        c.argument('deployment', help="deployment name")
        c.argument('name', help="endpoint name")
        c.argument('type', help="the type of the endpoint: online or batch")

    with self.argument_context('ml endpoint delete') as c:
        add_common_params(c)
        c.argument('deployment', help="deployment name")
        c.argument('name', help="endpoint name")
        c.argument('type', help="the type of the endpoint: online or batch")
