# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from knack.help_files import helps


def get_job_help():
    helps['ml job download'] = """
        type: command
        short-summary: "Downloads job related files into user home directory."
    """
    helps['ml job stream'] = """
            type: command
            short-summary: "Streams job logs into the console."
        """
