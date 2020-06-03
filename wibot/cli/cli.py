# -*- coding: utf-8 -*-

"""Console script for wibot."""
import click
import sys
#from wibot.cli.admin.cdot import cdot as admin_cdot
#from wibot.cli.admin.pure import pure as admin_pure
#from wibot.cli.admin.solidfire import solidfire as admin_solidfire
#from wibot.cli.admin.mode7 import mode7 as admin_mode7
#from wibot.cli.compute.solidfire import solidfire as compute_solidfire
#from wibot.cli.customer.cdot import cdot as customer_cdot
#from wibot.cli.admin.snow import snow as admin_snow
from wibot.cli.firewall.health import health as firewall_health
from wibot.cli.firewall.aclsearch import aclsearch as firewall_aclsearch
from wibot.cli.firewall.cpualert import cpualert as firewall_cpualert
from wibot.cli.firewall.captures import captures as firewall_captures
from wibot.cli.firewall.contexts import contexts as firewall_contexts
from wibot.cli.firewall.intbuffer import intbuffer as firewall_intbuffer
from wibot.cli.firewall.embaudit import embaudit as firewall_embaudit
from wibot.cli.firewall.pwrscan import pwrscan as firewall_pwrscan
from wibot.cli.firewall.fragment import fragment as firewall_fragment
from wibot.cli.firewall.codescan import codescan as firewall_codescan
from wibot.cli.firewall.firewall_cfgdiff import cfgdiff as firewall_cfgdiff

@click.group(name='admin', help="Storage team commands")
def admin(args=None):
    pass


@click.group(name='compute', help="Compute team commands")
def compute(args=None):
    pass


@click.group(name='customer', help="Customer executable commands")
def customer(args=None):
    pass

@click.group(name='firewall')
def firewall(args=None):
	"""
	For detailed usage instructions 
	Please refer: https://wiki.cisco.com/display/AS13445/Usage+Guide
	"""
	pass

#admin.add_command(admin_snow)
#admin.add_command(admin_mode7)
#admin.add_command(admin_cdot)
#admin.add_command(admin_pure)
#admin.add_command(admin_solidfire)

#compute.add_command(compute_solidfire)

#customer.add_command(customer_cdot)


firewall.add_command(firewall_health)
firewall.add_command(firewall_intbuffer)
firewall.add_command(firewall_contexts)
firewall.add_command(firewall_aclsearch)
firewall.add_command(firewall_cpualert)
firewall.add_command(firewall_captures)
firewall.add_command(firewall_embaudit)
firewall.add_command(firewall_pwrscan)
firewall.add_command(firewall_fragment)
firewall.add_command(firewall_codescan)
firewall.add_command(firewall_cfgdiff)

if __name__ == "__main__":
    sys.exit()  # pragma: no cover
