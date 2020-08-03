import click
from wibot.cli.firewall.f5_feed import ip_feed_wl
from wibot.cli.firewall.f5_feed import display_feed



@click.group(help="Add IP/Subnet to Whitelist on FeedServer")
def feed_wl():
	pass
@feed_wl.command(help="Add IP/Subnet to Whitelist on FeedServer")
@click.argument('ip')
@click.argument('org')
def feed_wl(ip,org):
	ip_feed_wl(ip,org)