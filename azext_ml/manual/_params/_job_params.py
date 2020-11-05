# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._common_params import add_common_params


def add_job_common_params(c):
    c.argument('name', help="Name of the job.")


def load_job_params(self):
    with self.argument_context('ml job create') as c:
        add_common_params(c)
        c.argument('file', help="yaml file to generate code job from")
        c.argument('save_as', help="file to save code job to")

    with self.argument_context('ml job download') as c:
        add_common_params(c)
        add_job_common_params(c)
        c.argument('all', help="All files generated in the job including outputs.")
        c.argument('download_path', help="If not specified will be downloaded into the current dir.")

    with self.argument_context('ml job stream') as c:
        add_common_params(c)
        add_job_common_params(c)
