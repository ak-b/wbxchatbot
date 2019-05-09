import click
from wistorage.infradb.pure import fetch_pure_clusters
from wiutil.pprint import print_table


@click.group(help="Pure storage commands")
def pure():
    pass


@pure.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster.lower(), fetch_pure_clusters()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))
