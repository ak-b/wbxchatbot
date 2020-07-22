import click
from wibot.cli.firewall.search_ipi_shell import lookup_ipi


@click.group(help="To search if an IP is blocked in the IP intelligence DB")
def search_ipi():
	pass

@search_ipi.command(help="To search if an IP is blocked in the IP intelligence DB")
@click.argument('ip_address')
def search_ipi(ip_address):
	lookup_ipi(ip_address)
	
