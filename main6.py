import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.1', username='admin', password='123456')
stdin, stdout, stderr = client.exec_command('/ip firewall filter add chain=forward src-mac-address=aa:bb:cc:dd:ee:ff action=drop')

for line in stdout:
    print(line.strip('\n'))
client.close()