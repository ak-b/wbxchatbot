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

@solidfire.command(name="nodes", help="Get nodes on solidfire cluster")
@click.option('--username', default=SOLIDFIRE_USERNAME, type=str)
@click.option('--password', default=SOLIDFIRE_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def nodes(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    solidfire = SolidFire(hostname, username, password)
    print_table(solidfire.nodes)


@solidfire.command(name="health", help="Get overall health of the solidfire cluster")
@click.option('--username', default=SOLIDFIRE_USERNAME, type=str)
@click.option('--password', default=SOLIDFIRE_PASSWORD, type=str)
@click.argument('hostname', nargs=1)
def health(username, password, hostname):
    if not username or not password:
        print('Insufficient credentials')
        sys.exit(1)

    solidfire = SolidFire(hostname, username, password)
    print_table(solidfire.health)
