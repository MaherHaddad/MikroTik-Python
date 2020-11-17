#!/usr/bin/env python

from netmiko import ConnectHandler
import time

MT1 = {
    'device_type': 'mikrotik_routeros',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': '',
}

MT2 = {
    'device_type': 'mikrotik_routeros',
    'ip': '192.168.1.2',
    'username': 'admin',
    'password': '',
}

all_devices = [MT1, MT2]
for devices in all_devices:
    print(f'Connecting to {devices["ip"]}')
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('ip address print')
    print(output)
    time.sleep(2)
