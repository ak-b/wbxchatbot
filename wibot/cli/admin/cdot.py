import click
from wistorage.infradb.cdot import fetch_all_cdots
from wiutil.pprint import print_table


@click.group(help="cDOT storage commands")
def cdot():
    pass


@cdot.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster['name'].lower(), fetch_all_cdots()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))

