import click
from wibot.cli.firewall.show_buffer import show_buffer


@click.group()
def intbuffer():
	pass

@click.command(help = "View Interface Buffer Status")
@click.argument('devicename')
def intbuffer(devicename):
	show_buffer(devicename)