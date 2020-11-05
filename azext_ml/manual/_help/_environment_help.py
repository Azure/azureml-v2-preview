# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from knack.help_files import helps


def get_environment_help():
    helps['ml environment'] = """
        type: group
        short-summary: ml environment
    """
    helps['ml environment list'] = """
        type: command
        short-summary: "Lists all environments in the workspace."
    """
    helps['ml environment show'] = """
            type: command
            short-summary: "Get the specified environment."
        """
    helps['ml environment create'] = """
                type: command
                short-summary: "Create environment."
            """
