from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

def connect(device):
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    return net_connect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_tier1_ipv4", methods = ["GET", "POST"])
def add_tier1_ipv4():
    if request.method == "POST" :
        r1_int = request.form["r1_int"]
        r1_ip = request.form["r1_ip"]
        r1_neighbor_ip = request.form["r1_neighbor_ip"]
        remote_as = request.form["remote_as"]

        env = Environment(loader=FileSystemLoader('jinja_templates'))
        template = env.get_template('tier1_bgp_template_cisco_ios.j2')

        R1_config = template.render(name = r1_int, ip = r1_ip, neighbor_ip = r1_neighbor_ip, remote_as=remote_as)

        output_file = f"configs/R1_EBGP_config.txt"
        with open(output_file, "w") as file:
            file.write(R1_config) 

        device_ips = {
                    "R1" : "192.168.10.11",
        }


        for device_name, ip in device_ips.items():
            device_details = {
                            'device_type': 'cisco_ios',
                            'ip' : ip,
                            'username' : 'sarang',
                            'password' : 'sarang',
            }
            hdl = connect(device_details)
            output_file = f'configs/{device_name}_EBGP_config.txt'
            hdl.send_config_from_file(output_file)

        return redirect(url_for("home"))

    return render_template("tier1_ipv4_details.html")

@app.route("/add_tier3_ipv4", methods = ["GET", "POST"])
def add_tier3_ipv4():
    if request.method == "POST" :
        r5_int = request.form["r5_int"]
        r5_ip = request.form["r5_ip"]
        r5_neighbor_ip = request.form["r5_neighbor_ip"]
        remote_as = request.form["remote_as"]

        env = Environment(loader=FileSystemLoader('jinja_templates'))
        template = env.get_template('tier3_bgp_template_cisco_ios.j2')

        R5_config = template.render(name = r5_int, ip = r5_ip, neighbor_ip = r5_neighbor_ip, remote_as=remote_as)

        output_file = f"configs/R5_EBGP_config.txt"
        with open(output_file, "w") as file:
            file.write(R5_config) 

        device_ips = {
                    "R5" : "192.168.10.31",
        }

        for device_name, ip in device_ips.items():
            device_details = {
                            'device_type': 'cisco_ios',
                            'ip' : ip,
                            'username' : 'sarang',
                            'password' : 'sarang',
            }
            hdl = connect(device_details)
            output_file = f'configs/{device_name}_EBGP_config.txt'
            hdl.send_config_from_file(output_file)

        return redirect(url_for("home"))

    return render_template("tier3_ipv4_details.html")

@app.route("/add_tier1_ipv6", methods = ["GET", "POST"])
def add_tier1_ipv6():
    if request.method == "POST" :
        r1_int = request.form["r1_int"]
        r1_ip = request.form["r1_ipv6"]
        r1_neighbor_ip = request.form["r1_neighbor_ipv6"]
        remote_as = request.form["remote_as"]

        env = Environment(loader=FileSystemLoader('jinja_templates'))
        template = env.get_template('tier1_bgp_ipv6_template_cisco_ios.j2')

        R1_config = template.render(name = r1_int, ip = r1_ip, neighbor_ip = r1_neighbor_ip, remote_as=remote_as)

        output_file = f"configs/R1_EBGP_IPv6_config.txt"
        with open(output_file, "w") as file:
            file.write(R1_config) 

        device_ips = {
                    "R1" : "192.168.10.11",
        }


        for device_name, ip in device_ips.items():
            device_details = {
                            'device_type': 'cisco_ios',
                            'ip' : ip,
                            'username' : 'sarang',
                            'password' : 'sarang',
            }
            hdl = connect(device_details)
            output_file = f'configs/{device_name}_EBGP_IPv6_config.txt'
            hdl.send_config_from_file(output_file)

        return redirect(url_for("home"))

    return render_template("tier1_ipv6_details.html")

@app.route("/add_tier3_ipv6", methods = ["GET", "POST"])
def add_tier3_ipv6():
    if request.method == "POST" :
        r5_int = request.form["r5_int"]
        r5_ip = request.form["r5_ipv6"]
        r5_neighbor_ip = request.form["r5_neighbor_ipv6"]
        remote_as = request.form["remote_as"]

        env = Environment(loader=FileSystemLoader('jinja_templates'))
        template = env.get_template('tier3_bgp_ipv6_template_cisco_ios.j2')

        R5_config = template.render(name = r5_int, ip = r5_ip, neighbor_ip = r5_neighbor_ip, remote_as=remote_as)

        output_file = f"configs/R5_EBGP_IPv6_config.txt"
        with open(output_file, "w") as file:
            file.write(R5_config) 

        device_ips = {
                    "R5" : "192.168.10.31",
        }

        for device_name, ip in device_ips.items():
            device_details = {
                            'device_type': 'cisco_ios',
                            'ip' : ip,
                            'username' : 'sarang',
                            'password' : 'sarang',
            }
            hdl = connect(device_details)
            output_file = f'configs/{device_name}_EBGP_IPv6_config.txt'
            hdl.send_config_from_file(output_file)

        return redirect(url_for("home"))

    return render_template("tier3_ipv6_details.html")


if __name__ =="__main__":
    app.debug = True 
    app.run(host='127.0.0.1', port=80)