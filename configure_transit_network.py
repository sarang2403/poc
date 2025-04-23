import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

def connect(device):
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    return net_connect

def main():

    device_ips = {
                    "R1" : "192.168.10.11",
                    "R3" : "192.168.10.21",
                    "R5" : "192.168.10.31",
    }
    
    #IPv4 Configuration
    with open('base_config_ipv4.yaml') as file:
        data = yaml.safe_load(file)

    #Create Configuration Files for IPv4
    env = Environment(loader=FileSystemLoader('jinja_templates'))
    template = env.get_template('ipv4_template_cisco_ios.j2')
    for hostname, interfaces in data["devices"].items():
        config = template.render(interfaces = interfaces)

        output_file = f"configs/{hostname}_ipv4_config.txt"
        with open(output_file, "w") as file:
            file.write(config) 

    #Configure IPv4 on ISP Core
    for device_name, ip in device_ips.items():
        device_details = {
                        'device_type': 'cisco_ios',
                        'ip' : ip,
                        'username' : 'sarang',
                        'password' : 'sarang',
        }
        hdl = connect(device_details)
        output_file = f'configs/{device_name}_ipv4_config.txt'
        #This configures the Interface + OSPF + MPLS Configuration 
        hdl.send_config_from_file(output_file)
    
    #IPv6 Configuration
    with open('base_config_ipv6.yaml') as file:
        data = yaml.safe_load(file)

    #Create Configuration Files for IPv6
    env = Environment(loader=FileSystemLoader('jinja_templates'))
    template = env.get_template('ipv6_template_cisco_ios.j2')
    for hostname, interfaces in data["devices"].items():
        config = template.render(interfaces = interfaces)

        output_file = f"configs/{hostname}_ipv6_config.txt"
        with open(output_file, "w") as file:
            file.write(config) 

    #Configure IPv6 on ISP Core
    for device_name, ip in device_ips.items():
        device_details = {
                        'device_type': 'cisco_ios',
                        'ip' : ip,
                        'username' : 'sarang',
                        'password' : 'sarang',
        }
        hdl = connect(device_details)
        output_file = f'configs/{device_name}_ipv6_config.txt'
        #This configures the IPv6 Interface Configuration
        hdl.send_config_from_file(output_file)

    #Configure IBGP for both IPv4 and IPv6
    for device_name, ip in device_ips.items():
        device_details = {
                        'device_type': 'cisco_ios',
                        'ip' : ip,
                        'username' : 'sarang',
                        'password' : 'sarang',
        }
        hdl = connect(device_details)
        
        #This configures the IBGP Configuration for IPv4 on Tier-1 Edge
        if ip ==  '192.168.10.11' :
            hdl.send_config_from_file('configs/t1_edge_ibgp.txt')

        #This configures the IBGP Configuration for IPv4 on Tier-3 Edge
        if ip == '192.168.10.31' :
            hdl.send_config_from_file('configs/t3_edge_ibgp.txt')    


if __name__ == "__main__":
    main()

