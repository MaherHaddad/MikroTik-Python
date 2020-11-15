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

with open('Rules') as f:
    lines = f.read().splitlines()
    print(lines)


all_devices = [MT1, MT2]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

