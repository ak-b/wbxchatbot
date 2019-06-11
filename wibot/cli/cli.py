# -*- coding: utf-8 -*-

"""Console script for wibot."""
import click
import sys
from wibot.cli.admin.cdot import cdot as admin_cdot
from wibot.cli.admin.pure import pure as admin_pure
from wibot.cli.admin.solidfire import solidfire as admin_solidfire
from wibot.cli.admin.mode7 import mode7 as admin_mode7
from wibot.cli.compute.solidfire import solidfire as compute_solidfire
from wibot.cli.customer.cdot import cdot as customer_cdot


@click.group(name='admin', help="Storage team commands")
def admin(args=None):
    pass


@click.group(name='compute', help="Compute team commands")
def compute(args=None):
    pass


@click.group(name='customer', help="Customer executable commands")
def customer(args=None):
    pass


admin.add_command(admin_mode7)
admin.add_command(admin_cdot)
admin.add_command(admin_pure)
admin.add_command(admin_solidfire)

compute.add_command(compute_solidfire)

customer.add_command(customer_cdot)

if __name__ == "__main__":
    sys.exit()  # pragma: no cover
