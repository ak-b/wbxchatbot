import click
import requests
from wibot.cli.firewall.cpuwatch import cpuwatch

@click.group()
def cpualert():
	pass

@cpualert.command(help = "List of devices where CPU crossed xx% in the past 24hrs")
@click.argument('threshold')
def cpualert(threshold):
	cpuwatch(threshold)