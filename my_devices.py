from getpass import getpass
pwd = getpass()
cisco3 = { 'host': 'cisco3.lasthop.io', 'username': 'pyclass', 'password': pwd, 'device_type': 'cisco_ios'}
arista1 = { 'host': 'arista1.lasthop.io', 'username': 'pyclass','password': pwd, 'device_type': 'arista_eos', 'global_delay_factor': 4}
#nxos1 = { 'host': '1.lasthop.io', 'username': 'pyclass','password': pwd, 'device_type': 'cisco_nxos'}
arista2 = { 'host': 'arista2.lasthop.io', 'username': 'pyclass','password': pwd, 'device_type': 'arista_eos', 'global_delay_factor': 4}
srx2 = { 'host': 'srx2.lasthop.io', 'username': 'pyclass','password': pwd, 'device_type': 'juniper_junos'}

devices = [cisco3, arista1, arista2, srx2]
