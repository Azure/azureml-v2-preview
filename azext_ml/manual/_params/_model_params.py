# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def load_model_params(self):
    with self.argument_context('ml model create') as c:
        add_common_params(c)
        c.argument(
            'name', help="The name under which the model should be registered")
        c.argument('file', help="The yaml file containing the entity’s AzureML specification.")
        c.argument(
            'path', help="The path to model assets. It can be either a file, or a directory.")

    with self.argument_context('ml model show') as c:
        add_common_params(c)
        c.argument('name', help="Instead of the –id parameter, the name of the resource can be provided to which the operation should be applied.")

    with self.argument_context('ml model list') as c:
        add_common_params(c)
        c.argument('filter', help="A filter expression to filter the list of assets returned. we have yet to define the filter expression language to support. On a high level the asset type will be filtered by the noun on which the list operation is executed (e.g. az ml component list). In addition, we will need filtering by name, tags, label, type (in the case of component), creation_context.created_by, creation_context.created_time (range), asset.creation_context.created_by, asset.id, asset.tags, and probably a few more.")
