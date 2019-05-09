# -*- coding: utf-8 -*-

"""Console script for wibot."""
import sys

import click

from wibot.cli.admin.cdot import cdot
from wibot.cli.admin.pure import pure
from wibot.cli.admin.solidfire import solidfire as admin_solidfire
from wibot.cli.compute.solidfire import solidfire


@click.group(name='admin')
def admin(args=None):
    pass


@click.group(name='compute')
def compute(args=None):
    pass


admin.add_command(cdot)
admin.add_command(pure)
admin.add_command(admin_solidfire)

compute.add_command(solidfire)

if __name__ == "__main__":
    sys.exit(admin())  # pragma: no cover
