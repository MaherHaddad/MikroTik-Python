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

with open('Firewall') as f:
    lines = f.read().splitlines()


all_devices = [MT1, MT2]
for devices in all_devices:
    print(f'Connecting to {devices["ip"]}')
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(f'These firewall rules have been installed on {devices["ip"]} ')
    net_connect = ConnectHandler(**devices)
    output1 = net_connect.send_command('ip firewall export')
    print(output1)
    time.sleep(2)

