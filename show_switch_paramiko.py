#SSH to device using Paramiko
#execute and print show command

import paramiko

ip_address = '1.2.3.4'
username = 'admin'
password = 'password'

print '\n------------------------------------------------------'
print '--- Attempting to connect to: ', ip_address

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,
                   username=username,
                   password=password)


print '--- Success! connecting to: ', ip_address
print '------------------------------------------------------\n'

stdin, stdout, stderr = ssh_client.exec_command('show switch')
show_switch = stdout.readlines()

print show_switch

ssh_client.close()
