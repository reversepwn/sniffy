from scapy.all import *
from termcolor import colored
import sys
import netifaces

target_ip = sys.argv[1]
show_all = "--more" in sys.argv
iface = sys.argv[3] if len(sys.argv) > 3 else None

def process_packet(packet):
    if IP in packet and packet[IP].src == target_ip:
        print(colored("[SENT]:", "green"))
        print(f"From: Target ({target_ip})")
        print(f"To: {packet[IP].dst}")
        if show_all:
            print("-" * 50)
            print(colored("[OTHER]:", "yellow"))
            print(colored(str(packet), "yellow"))
        print("-" * 50)
    elif IP in packet and packet[IP].dst == target_ip:
        print(colored("[RECEIVED]:", "blue"))
        print(f"From: {packet[IP].src}")
        print(f"To: Target ({target_ip})")
        if show_all:
            print("-" * 50)
            print(colored("[OTHER]:", "yellow"))
            print(colored(str(packet), "yellow"))
        print("-" * 50)

print(colored(f"Sniffy, made by puffer", "red"))
if iface:
    addrs = netifaces.ifaddresses(iface)
    if netifaces.AF_INET not in addrs:
        print(colored(f"Error: {target_ip} is not available on {iface}", "red"))
        sys.exit(1)
    else:
        ip = addrs[netifaces.AF_INET][0]["addr"]
        if ip != target_ip:
            print(colored(f"Error: {target_ip} is not available on {iface}", "red"))
            sys.exit(1)
    print(colored(f"Sniffing target ({target_ip}) on interface {iface}...", "yellow"))
else:
    print(colored(f"Sniffing target ({target_ip}) on all interfaces...", "yellow"))
sniff(filter=f"ip and (src host {target_ip} or dst host {target_ip})",
      prn=process_packet,
      iface=iface,
      timeout=60)

