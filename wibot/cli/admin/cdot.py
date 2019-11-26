import click
#from wistorage.core.netapp import FilerCDOT
#from wistorage.infradb.cdot import *
#from wiutil.pprint import print_table
#from wiutil.pprint import bytes_to_str
from wibot import NETAPP_USERNAME, NETAPP_PASSWORD


@click.group(help="cDOT storage commands")
def cdot():
    pass


@cdot.command(help="Inventory from infradb")
def inventory():
    clusters = list(map(lambda cluster: cluster['name'].lower(), fetch_all_cdots()))
    clusters.sort()
    print_table(list(map(lambda cluster: {'name': cluster}, clusters)))


@cdot.command(name="tenant-user-group-volumes")
@click.argument("tenant_id", nargs=1)
@click.argument("usergroup_id", nargs=1)
def tenant_usergroup_volumes(tenant_id, usergroup_id):
    """
    List volumes belonging to a tenant and user group \n
    :param tenant_id: Tenant ID \n
    :param usergroup_id: Usergroup ID \n
    :return: List of volumes
    """
    volumes = fetch_cdot_tenant_user_volume_info(tenant_id, usergroup_id)
    vol_list = list(map(lambda vol: {'name': vol['name'], 'size': vol['size'],
                                     'aggregate': vol['netapp_cdot_aggregate']['name'],
                                     'cluster': vol['netapp_cdot_aggregate']
                                     ['netapp_cdot_node']['netapp_cdot_cluster']['name']}, volumes))
    print_table(vol_list)


@cdot.command(name="vol-tenant-user-group")
@click.argument("data_lif", nargs=1)
@click.argument("vol_name", nargs=1)
def vol_tenant_usergroup_id(data_lif, vol_name):
    """
    Get Tenant and Usergroup ID for a cDOT volume in InfraDB \n
    :param data_lif: NFS server IP or FQDN (cDOT Data LIF) \n
    :param vol_name: Name of the volume \n
    :return: Tenant ID and Usergroup ID
    """
    vol_info_list = list()
    vol_id = fetch_cdot_volume_id_using_datalif(vol_name, data_lif)
    if not vol_id:
        print("Volume id not found for datalif {} and vol name {}".format(data_lif, vol_name))
    else:
        vol_info = fetch_cdot_volume_info(vol_id)
        del vol_info['netapp_cdot_aggregate']
        vol_info_list.append(vol_info)
        print_table(vol_info_list)


@cdot.command(name="update-vol-tenant-user-group")
@click.argument("data_lif", nargs=1)
@click.argument("vol_name", nargs=1)
@click.argument("tenant_id", nargs=1)
@click.argument("usergroup_id", nargs=1)
def vol_tenant_usergroup_id_update(data_lif, vol_name, tenant_id, usergroup_id):
    """
    Update Tenant and Usergroup ID for a cDOT volume in InfraDB \n
    :param data_lif: NFS server IP or FQDN (cDOT Data LIF) \n
    :param vol_name: Name of the volume \n
    :param tenant_id: Tenant ID \n
    :param usergroup_id: Usergroup ID \n
    :return: old and new values for volume \n
    """
    vol_info_list = list()
    vol_id = fetch_cdot_volume_id_using_datalif(vol_name, data_lif)
    if not vol_id:
        print("Volume id not found for datalif {} and vol name {}".format(data_lif, vol_name))
    else:
        vol_info = fetch_cdot_volume_info(vol_id)
        vol_info['state'] = "old"
        del vol_info['netapp_cdot_aggregate']
        del vol_info['id']
        vol_info_list.append(vol_info)

        if vol_info['tenant_id'] == tenant_id and vol_info['user_group_id'] == usergroup_id:
            print("Volume already has required tenant and usergroup details set")
        else:
            update_cdot_volume_tenantid_usergroupid(vol_id, tenant_id, usergroup_id)
            vol_info = fetch_cdot_volume_info(vol_id)
            vol_info['state'] = "new"
            del vol_info['netapp_cdot_aggregate']
            del vol_info['id']
            vol_info_list.append(vol_info)
            print_table(vol_info_list)


@cdot.command(name="qtree-tenant-user-group")
@click.argument("data_lif", nargs=1)
@click.argument("qtree_name", nargs=1)
def qtree_tenant_usergroup_id(data_lif, qtree_name):
    """
    Get Tenant and Usergroup ID for a cDOT qtree in InfraDB \n
    :param data_lif: NFS server IP or FQDN (cDOT Data LIF) \n
    :param qtree_name: Name of the qtree \n
    :return: Tenant ID and Usergroup ID
    """
    qtree_info_list = list()
    qtree_id = fetch_cdot_qtree_id_using_datalif(qtree_name, data_lif)
    if not qtree_id:
        print("qtree id not found for datalif {} and qtree name {}".format(data_lif, qtree_name))
    else:
        qtree_info = fetch_cdot_qtree_info(qtree_id)
        del qtree_info['netapp_cdot_volume']
        qtree_info_list.append(qtree_info)
    print_table(qtree_info_list)


@cdot.command(name="update-qtree-tenant-user-group")
@click.argument("data_lif", nargs=1)
@click.argument("qtree_name", nargs=1)
@click.argument("tenant_id", nargs=1)
@click.argument("usergroup_id", nargs=1)
def qtree_tenant_usergroup_id_update(data_lif, qtree_name, tenant_id, usergroup_id):
    """
    Update Tenant and Usergroup ID for a cDOT qtree in InfraDB \n
    :param data_lif: NFS server IP or FQDN (cDOT Data LIF) \n
    :param qtree_name: Name of the qtree \n
    :param tenant_id: Tenant ID \n
    :param usergroup_id: Usergroup ID \n
    :return: old and new values for qtree \n
    """
    qtree_info_list = list()
    qtree_id = fetch_cdot_qtree_id_using_datalif(qtree_name, data_lif)
    if not qtree_id:
        print("qtree id not found for datalif {} and qtree name {}".format(data_lif, qtree_name))
    else:
        qtree_info = fetch_cdot_qtree_info(qtree_id)
        qtree_info['state'] = "old"
        del qtree_info['netapp_cdot_volume']
        del qtree_info['id']
        qtree_info_list.append(qtree_info)

        if qtree_info['tenant_id'] == tenant_id and qtree_info['user_group_id'] == usergroup_id:
            print("qtree already has required tenant and usergroup details set")
        else:
            update_cdot_qtree_tenantid_usergroupid(qtree_id, tenant_id, usergroup_id)
            qtree_info = fetch_cdot_qtree_info(qtree_id)
            qtree_info['state'] = "new"
            del qtree_info['netapp_cdot_volume']
            del qtree_info['id']
            qtree_info_list.append(qtree_info)
    print_table(qtree_info_list)


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
