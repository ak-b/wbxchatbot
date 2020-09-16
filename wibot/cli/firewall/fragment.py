import click
from wibot.cli.firewall.check_fragment import frag

@click.group()
def fragment():
	pass

@click.command(help="Runs Fragment Stats on the Core Context in LHR and SJC cluster FWs")
def fragment():
	devices = ['','']
	print("Running Fragment Stats on the Core Context in LHR and SJC cluster FWs")
	for device in devices:
		print("=============")
		print("Current IP fragment database statistics for all interfaces on {}".format(device))
		print("=============")
		frag(device)
		print("\n")
