#!/usr/bin/env python

from netmiko import ConnectHandler

MT1 = {
    'device_type': 'mikrotik_routeros',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': '123456',
}

MT2 = {
    'device_type': 'mikrotik_routeros',
    'ip': '192.168.1.253',
    'username': 'admin',
    'password': '123456',
}

all_devices = [MT1, MT2]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('ip address add address=1.1.1.4/24 interface=ether3')
    print(output)
