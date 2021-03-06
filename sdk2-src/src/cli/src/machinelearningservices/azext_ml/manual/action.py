# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import argparse
from knack.util import CLIError


class OverridePropertiesBySet(argparse._AppendAction):  # pylint: disable=protected-access
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(OverridePropertiesBySet, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        kwargs = {}
        for item in values:
            try:
                key, value = item.split("=", 1)
                kwargs[key] = value
            except ValueError:
                raise CLIError("usage error: {} KEY=VALUE [KEY=VALUE ...]".format(option_string))
        return kwargs
