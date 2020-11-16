import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.1', username='admin', password='')
stdin, stdout, stderr = client.exec_command('ip dhcp-client add disabled=no interface=ether5')
stdin, stdout, stderr = client.exec_command('ip service set telnet disabled=yes')
stdin, stdout, stderr = client.exec_command('ip service set ftp disabled=yes')
stdin, stdout, stderr = client.exec_command('export')

for line in stdout:
    print(line.strip('\n'))
client.close()