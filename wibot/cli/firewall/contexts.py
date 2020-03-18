import click
from wibot.cli.firewall.captures_report import extract_contexts as show_ctx

@click.group()
def contexts():
	pass

@contexts.command(help = "View Contexts")
@click.argument('device')
def contexts(device):
	print("Contexts on firewall {}".format(device))
	print("==>")
	fw_contexts = show_ctx(device)
	for item in fw_contexts:
		print(item)