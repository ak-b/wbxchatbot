import click
from wistorage.core.netapp import FilerCDOT
from wistorage.infradb.cdot import fetch_all_cdots
from wiutil.pprint import print_table
from wiutil.pprint import bytes_to_str
from wibot import NETAPP_USERNAME, NETAPP_PASSWORD


@click.group(help="cDOT storage commands")
def cdot():
    pass


@cdot.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster['name'].lower(), fetch_all_cdots()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))


@cdot.command(help="List the health on a NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def health(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    print("Health Status:", filer.health)


@cdot.command(help="List the nodes for NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def nodes(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    print_table(filer.nodes)


@cdot.command(help="List the interfaces for NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def interfaces(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    print_table(filer.interfaces)


@cdot.command(help="Show capacity for NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def capacity(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    print_table(filer.capacity)


@cdot.command(help="Show the disks for NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def disks(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    total, spare, failed = filer.disks
    print_table([{'total': total, 'spare': spare, 'failed': failed}])


@cdot.command(help="List the aggregates on a NetApp cDOT filer")
@click.argument('hostname', nargs=1)
def aggregates(hostname):
    filer = FilerCDOT(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    aggr_list = list()
    for aggr in filer.aggregates:
        aggr_info = {
            'name': aggr.name,
            'is-root': 'true' if aggr.is_root else 'false',
            'total_size': bytes_to_str(aggr.total_size),
            'current_size': bytes_to_str(aggr.current_size),
            'utilization': aggr.utilization,
            'disks': aggr.disk_count,
            'node': aggr.node
        }
        aggr_list.append(aggr_info)

    print_table(aggr_list)
