import click
from wibot import NETAPP_USERNAME, NETAPP_PASSWORD
from wistorage.core.netapp import FilerCDOT
from wistorage.infradb.cdot import fetch_all_cdots, fetch_cdot_tenant_user_volume_info, \
    fetch_cdot_volume_id_using_datalif, fetch_cdot_qtree_id_using_datalif, fetch_cdot_volume_info, fetch_cdot_qtree_info
from wiutil.pprint import print_table


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
    tenant_id: Tenant ID \n
    usergroup_id: Usergroup ID \n
    List of volumes
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
        cluster_name = vol_info['netapp_cdot_aggregate']['netapp_cdot_node']['netapp_cdot_cluster']['name']
        del vol_info['netapp_cdot_aggregate']
        filer = FilerCDOT(cluster_name, NETAPP_USERNAME, NETAPP_PASSWORD)
        volume = list(filter(lambda vol: vol.name == vol_name, filer.volumes))
        vol_utilization = volume[0].utilization if volume else None
        vol_info['utilization'] = round(vol_utilization,2)
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
