#usr/bin/env python
#coding utf-8

_author_ = "mpinizzotto"
	
#######################################################
#script to configure a list of devices via ssh cmd line
#######################################################

import paramiko

ssh_client = paramiko.SSHClient()

"""
change these variables
"""

dev_list = ['ipaddr','ipaddr']
username = 'myuser'
password = 'mypass'
command = 'my cmd'


def connect(ip,username,password):
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,
                       username=username,
                       password=password)


def config_edges():
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.readlines()
    return output


def main():

    for ip in dev_list:
        connect(ip,username,password)
        response = config_edges()
        print ip + " " + command + " success"


if __name__ == '__main__':
    main()
