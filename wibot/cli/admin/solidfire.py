import click
from wistorage.core.solidfire import SolidFire
from wistorage.infradb.solidfire import fetch_solidfire_clusters
from wiutil.pprint import bytes_to_str
from wiutil.pprint import print_table

from wibot import SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD


@click.group(help="Solidfire storage commands")
def solidfire():
    pass


@solidfire.command(help="Global Inventory")
def inventory():
    clusters = list(map(lambda cluster: cluster.lower(), fetch_solidfire_clusters()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))


@solidfire.command(help="Cluster capacity")
@click.argument("cluster", nargs=1)
def capacity(cluster):
    sf = SolidFire(cluster, SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD)
    capacity = sf.capacity
    capacity['total'] = bytes_to_str(int(capacity['total']))
    capacity['used'] = bytes_to_str(int(capacity['used']))
    capacity['provisioned'] = bytes_to_str(int(capacity['provisioned']))
    print_table([capacity])


@solidfire.command(help="Utilization per volume")
@click.argument("cluster", nargs=1)
def utilization(cluster):
    sf = SolidFire(cluster, SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD)
    print_table(sf.volume_util)


@solidfire.command(name="nodes", help="Node information")
@click.argument('hostname', nargs=1)
def nodes(hostname):
    solidfire = SolidFire(hostname, SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD)
    print_table(solidfire.nodes)


@solidfire.command(name="health", help="Cluster health")
@click.argument('hostname', nargs=1)
def health(hostname):
    solidfire = SolidFire(hostname, SOLIDFIRE_USERNAME, SOLIDFIRE_PASSWORD)
    health = solidfire.health
    if health:
        print_table(solidfire.health)
    else:
        print("No alerts found")
