import click
from wibot.cli.firewall.f5_feed_remove import ip_remove_feed_wl
from wibot.cli.firewall.f5_feed_remove import display_feed


@click.group(help="Remove IP/Subnet from Whitelist on Feedserver")
def remove_feed():
	pass

@remove_feed.command(help="Remove IP/Subnet from Whitelist on Feedserver")
@click.argument('ip')
@click.argument('org')
def remove_feed(ip,org):
	ip_remove_feed_wl(ip,org)