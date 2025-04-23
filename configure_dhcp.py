import csv 
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import sys
from loguru import logger
import os
import time

def get_data():
    with open('inventory.csv', 'r') as file:
        inventory = list(csv.DictReader(file))
        return inventory

def render_template(template_file, data):
    env = Environment(loader=FileSystemLoader('jinja_templates'))
    template = env.get_template(template_file) 
    return template.render(devices = data)

def connect(device):
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    return net_connect

def main():
    template_file = 'dhcp_template_cisco_ios.j2'
    output_file = os.path.abspath('configs/dhcp_configuration')

    inventory = get_data()
    configuration = render_template(template_file, inventory)

    with open(output_file, 'w') as file : 
        file.write(configuration)

    dhcp_server = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.10.254',
        'username' : 'sarang',
        'password' : 'sarang',
    }

    hdl = connect(dhcp_server)
    try: 
        hdl.send_config_from_file(output_file)
        logger.success('Configured DHCP Server Successfully')
        time.sleep(30)

    except:
        sys.exit(1)

if __name__ == "__main__" :
    main() 
