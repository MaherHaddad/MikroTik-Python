import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router1 = {'hostname': '192.168.1.1', 'port': '22', 'username':'admin', 'password':''}
router2 = {'hostname': '192.168.1.2', 'port': '22', 'username':'admin', 'password':''}
router3 = {'hostname': '192.168.1.3', 'port': '22', 'username':'admin', 'password':''}

# creating a list of dictionaries (of devices)
routers = [router1, router2, router3]

# Doing a loop
for router in routers:
    print(f'Connecting to {router["hostname"]}')
    client.connect(**router)
    stdin, stdout, stderr = client.exec_command('routing ospf network add area=backbone')
    for line in stdout:
        print(line.strip('\n'))
    stdin, stdout, stderr = client.exec_command('routing ospf interface print')
    for line in stdout:
        print(line.strip('\n'))
    time.sleep(2)

client.close()