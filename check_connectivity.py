import subprocess
from loguru import logger
import csv 
import sys

def check_ping(ip):
    command = f"ping -c2 {ip}"
    output = subprocess.run(command, text=True, capture_output=True, shell=True)
    if output.returncode == 0 :
        logger.success(f"Ping to IP : {ip} successful")
        return 1
    else:
        logger.error(f"Failed to ping IP : {ip}")
        return 0

def get_data():
    with open('inventory.csv', 'r') as file:
        inventory = list(csv.DictReader(file))
        return inventory

def main():
    
    fail = 0
    inventory = get_data()
    for device in inventory :
        ip = device['ip']
        if not check_ping(ip) : 
            fail = 1 
    
    if fail :
        sys.exit(1)

if __name__ == "__main__":
    main()