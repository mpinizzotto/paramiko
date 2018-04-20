########################################################################################
# Use with CSV file
# Format with four rows which inlcude the hostname,ip adress, username and password
# iterates through list of devices and prints desired command/s
# pulls switch stack information
########################################################################################



import csv
import re
import paramiko

#--------------------------------------------------

device_info = {}
dev_list = []
ssh_client = paramiko.SSHClient()

#--------------------------------------------------

def read_from_csv(myfile):

    csvfile = open(myfile, 'r')
    csv_in = csv.reader(csvfile)
    for dev in csv_in:
        dev_list.append(dev)
    return dev_list
    csvfile.close()	

	
def connect(ip,username,password):
    
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,
                       username=username,
                       password=password)

def get_hardware_version():
    stdin, stdout, stderr = ssh_client.exec_command('show switch')
    output = stdout.readlines()		
    search_string = re.compile('.+(V[0-9]{2})(.+)')

    for lines in output:
        info = lines.strip()
        hardware_ver = search_string.search(info)
        if hardware_ver is not None:
            device_info['hardware_ver'] = hardware_ver.group(1)
        else:
	        continue
    
        print device_info['hardware_ver']
	

def get_sw_version():
    stdin, stdout, stderr = ssh_client.exec_command('show version')
    output = stdout.readlines()		
    search_string = re.compile('.+([0-9]{2}\.[0-9]{2}\.[0-9]{2}[aA-zZ])(.+)')
    for lines in output:
        info = lines.strip()
        sw_version = search_string.search(info)
        if sw_version is not None:
            device_info['sw_version'] = sw_version.group(1)
        else:
	        continue
    
    return device_info	
    #print 'device_info['sw_version']
	
def get_model():
    stdin, stdout, stderr = ssh_client.exec_command('show version | i Model Number')
    output = stdout.readlines()
    search_string = re.compile('Model Number(.+)([A-Z]{2}-[A-Z][0-9]{1,4}-.+)')
    for lines in output:
        info = lines.strip()
        model = search_string.search(info)
        if model is not None:
            device_info['model'] = model.group(2)
        else:
	        continue
    
    return device_info    
    #print 'Device Model: ', device_info['model']
	
					    
						
#-------------------------------------------------------------------
						
if __name__ == "__main__":

    read_from_csv('myswitch.csv')	

    for line in dev_list:

        device_info_list = line
        device_info['hostname'] = device_info_list[0]
        device_info['ip'] = device_info_list[1]
        device_info['username'] = device_info_list[2]
        device_info['password'] = device_info_list[3]
		
		
        print '---------------------------------------------------------------'
        print 'Hostname: ', device_info['hostname']
        connect(device_info['ip'],device_info['username'],device_info['password'])
        get_model()
        print "Model Number: ", device_info['model']
        connect(device_info['ip'],device_info['username'],device_info['password'])
        get_sw_version()
        print 'SW Version: ', device_info['sw_version']
        connect(device_info['ip'],device_info['username'],device_info['password'])
        print ""
        print 'Hardware Version/s: '
        get_hardware_version()
 

	
	
	
    
	
	
	
    
    
	
	
	
	
	