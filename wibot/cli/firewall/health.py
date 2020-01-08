import click
from wibot.cli.firewall.show_commands import run_show as show

@click.group(help='FW healthchecks',chain=True)
def health():
	pass

#@health.command('hi')
#def hi():
#	click.echo('Hello! I understand the following commands:')
#	click.echo('CPU')
#	click.echo('MEMORY')

@health.command('CPU')
@click.argument('devicename')
@click.argument('context')
def CPU(devicename,context):
	show(devicename,context,'CPU')

# print statements work under this construct

@health.command('MEMORY')
@click.argument('devicename')
@click.argument('context')
def MEMORY(devicename,context):
	show(devicename,context,'MEMORY')

@health.command('EMBCONN')
@click.argument('devicename')
@click.argument('context')
def EMBCONN(devicename,context):
	show(devicename,context,'EMBCONN')