import click
from wistorage.core.solidfire import SolidFire
from wistorage.infradb.solidfire import fetch_solidfire_clusters
from wiutil.pprint import bytes_to_str
from wiutil.pprint import print_table

from wibot import SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD


@click.group(help="Solidfire storage commands")
def solidfire():
    pass


@solidfire.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster.lower(), fetch_solidfire_clusters()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))


@solidfire.command(help="Capacity for a solidfire cluster")
@click.argument("cluster", nargs=1)
def capacity(cluster):
    sf = SolidFire(cluster, SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD)
    capacity = sf.capacity
    capacity['total'] = bytes_to_str(int(capacity['total']))
    capacity['used'] = bytes_to_str(int(capacity['used']))
    capacity['provisioned'] = bytes_to_str(int(capacity['provisioned']))
    print_table([capacity])
