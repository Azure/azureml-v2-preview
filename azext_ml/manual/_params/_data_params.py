# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def load_data_params(self):
    with self.argument_context('ml data list') as c:
        add_common_params(c)
        c.argument('name', help="Name of the data asset, can be in name:version format. If a version is not provided, all versions of the data asset will be listed.")

    with self.argument_context('ml data show') as c:
        add_common_params(c)
        c.argument('name', help="Name of the data asset, can be in name:version format. If a version is not provided, the latest version of the data asset will be provided.")

    with self.argument_context('ml data create') as c:
        add_common_params(c)
        c.argument('name', help="Name of the data asset, can be in name:version format. If a version is not provided, the command will create a data asset with version being latest version + 1")
        c.argument('description', help="Description of the data asset.")
        c.argument('file', help="The yaml file containing definition of the data asset.")

    with self.argument_context('ml data upload') as c:
        add_common_params(c)
        c.argument('name', help="Name of the data asset, can be in name:version format. If a version is not provided, the command will create a data asset with version being latest version + 1")
        c.argument('description', help="Description of the data asset.")
        c.argument('path', help="Local path pointing at the file/folder you want to upload and register as a data asset.")
        c.argument('datastore_name', help="Datastore where the data asset will be uploaded to, default to the default datastore associated with the Azure ML workspace.")

    with self.argument_context('ml data delete') as c:
        add_common_params(c)
        c.argument('name', help="Name of the data asset, can be in name:version format. If a version is not provided, all versions of the data asset will be deleted.")
