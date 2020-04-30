import click
import os
from wibot.cli.firewall.pwrscan_report import report 

@click.group(help = "Check PSU and Fan Health")
def pwrscan():
	pass

@pwrscan.command(help = "Check PSU and Fan Health")
@click.option('--device',help="Enter device name for pwrscan")
def pwrscan(device):
	report(device)