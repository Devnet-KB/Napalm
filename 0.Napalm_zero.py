# Introduction to Napalm. Notice the anotomy of code is similar to Netmiko.

from napalm import get_network_driver
import pprint

driver = get_network_driver('ios') # Device Type is IOS

device = driver(hostname='sandbox-iosxe-recomm-1.cisco.com',username='developer', password='C1sco12345',optional_args={'port':22})

#Open connection to the device
device.open()
 
#Facts about device
data=device.get_facts()
pprint.pprint(data)

# Capture running-config
data= device.get_config(retrieve='all', full=False, sanitized=False)['running']
with open ("config.txt",'w') as fo:
    fo.write(data)

#Close the connetion to the device
device.close()



#Other methods available
#################################################
#get_arp_table
#get_bgp_config
#get_bgp_neighbors()
#get_bgp_neighbors_detail(neighbor_address='')
#get_config(retrieve='all', full=False, sanitized=False)
#get_environment()
#get_facts()
#get_firewall_policies()
#get_interfaces()
#get_interfaces_counters()
#get_interfaces_ip()
#get_ipv6_neighbors_table()
#get_lldp_neighbors()
#get_lldp_neighbors_detail(interface='')
#get_mac_address_table()
#get_network_instances(name='')
#get_ntp_peers()
#get_ntp_servers()
#get_ntp_stats()
#get_optics()
#get_probes_config()
#get_probes_results()
#get_route_to(destination='', protocol='', longer=False)
#get_snmp_information()
#get_users()
#get_vlans()
#has_pending_commit()
#ping(destination, source='', ttl=255, timeout=2, size=100, count=5, vrf='', source_interface='')
#traceroute(destination, source='', ttl=255, timeout=2, vrf='')
