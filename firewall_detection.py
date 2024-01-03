import socket
import ipaddress
from scapy.all import *

def get_additional_info(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return "Unknown Hostname"

def check_firewall(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"The host {ip} is reachable on port {port}. A firewall may be allowing the connection.")
            
            hostname = get_additional_info(ip)
            print(f"Hostname: {hostname}")

            ip_address = socket.gethostbyname(hostname)
            print(f"IP Address: {ip_address}")

            ip_network = ipaddress.IPv4Network(f"{ip_address}/24", strict=False)
            print(f"IP Range: {ip_network.network_address} - {ip_network.broadcast_address}")

    except socket.error:
        print(f"The host {ip} is not reachable on port {port}. There might be a firewall blocking the connection.")

# Example of usage
target_ip = "192.168.1.1"  # Replace with the IP you want to check
target_port = 80  # Replace with the port you want to check

check_firewall(target_ip, target_port)
