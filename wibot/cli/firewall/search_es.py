import click
from wibot.cli.firewall.kibana_logs import search

@click.group(help="To Search for Embryonic Connection Logs")
def logs():
	pass 

@logs.command(help="To Search for Embryonic Connection Logs")
def logs():
	search()
	
