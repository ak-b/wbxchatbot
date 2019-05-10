import click
from wistorage.core.netapp import FilerCDOT
from wistorage.infradb.cdot import fetch_all_cdots
from wiutil.pprint import print_table
from wibot import NETAPP_USERNAME, NETAPP_PASSWORD

@click.group(help="cDOT storage commands")
def cdot():
    pass


@cdot.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster['name'].lower(), fetch_all_cdots()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))

@cdot.command(help="List total, spare and failed disk count on a NetApp cDOT filer")
@click.option('--username', default=NETAPP_USERNAME, type=str)
@click.option('--password', default=NETAPP_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def disks(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    filer = FilerCDOT(hostname, username, password)
    total, spare, failed = filer.disks
    print("total = {}, spare = {}, failed = {}".format(total, spare, failed))


@cdot.command(help="List the health on a NetApp cDOT filer")
@click.option('--username', default=NETAPP_USERNAME, type=str)
@click.option('--password', default=NETAPP_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def health(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    filer = FilerCDOT(hostname, username, password)
    print("Health Status:", filer.health)


@cdot.command(help="List the nodes for NetApp cDOT filer")
@click.option('--username', default=NETAPP_USERNAME, type=str)
@click.option('--password', default=NETAPP_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def nodes(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    filer = FilerCDOT(hostname, username, password)
    print_table(filer.nodes)


@cdot.command(help="List the interfaces for NetApp cDOT filer")
@click.option('--username', default=NETAPP_USERNAME, type=str)
@click.option('--password', default=NETAPP_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def interfaces(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    filer = FilerCDOT(hostname, username, password)
    print_table(filer.interfaces)
