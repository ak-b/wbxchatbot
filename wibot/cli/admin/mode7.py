import os

import click
from wistorage.core.errors import StorageDeviceError
from wistorage.core.netapp import Filer7Mode
from wiutil.pprint import bytes_to_str
from wiutil.pprint import print_table

NETAPP_USERNAME = os.environ.get('NETAPP_7MODE_USERNAME')
NETAPP_PASSWORD = os.environ.get('NETAPP_7MODE_PASSWORD')


@click.group("7mode", help="Run netapp 7 mode commands")
def mode7():
    pass


@mode7.command(help="List the aggregates on a NetApp 7mode filer")
@click.argument('hostname', nargs=1)
def aggregates(hostname):
    filer = Filer7Mode(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    aggr_list = list()
    for aggr in filer.aggregates:
        aggr_info = {
            'name': aggr.name,
            'total_size': bytes_to_str(aggr.total_size),
            'current_size': bytes_to_str(aggr.current_size),
            'utilization': aggr.utilization,
        }
        aggr_list.append(aggr_info)

    print_table(aggr_list)


@mode7.command(help="List the capacity on a NetApp 7Mode filer")
@click.argument('hostname', nargs=1)
def capacity(hostname):
    filer = Filer7Mode(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    cap_list = list()
    capacity = filer.capacity[0]
    cap_info = {
        'name': hostname,
        'Used Capacity': bytes_to_str(capacity['Used Capacity']),
        'Total Capacity': bytes_to_str(capacity['Total Capacity']),
        'Utilization': capacity['Utilization'],
    }
    cap_list.append(cap_info)
    print_table(cap_list)


@mode7.command(help="Total, spare and failed disk count")
@click.argument('hostname', nargs=1)
def disks(hostname):
    filer = Filer7Mode(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    total, spare, failed = filer.disks
    print_table([{'total': total, 'spare': spare, 'failed': failed}])


@mode7.command(help="Health status of NetApp 7mode filer")
@click.argument('hostname', nargs=1)
def health(hostname):
    filer = Filer7Mode(hostname, NETAPP_USERNAME, NETAPP_PASSWORD)
    status, errors = filer.health
    if status == StorageDeviceError.no_errors:
        print('ok')
    else:
        print('Not ok: check for errors in environment status output %s' % str(errors))
