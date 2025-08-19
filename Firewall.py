# simple_firewall.py
from scapy.all import sniff

# Blocked websites or IPs
blocked_ips = ["142.250.183.206"]  # example: google.com IP

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_dst = packet["IP"].dst
        if ip_dst in blocked_ips:
            print(f"Blocked: {ip_dst}")
        else:
            print(f"Allowed: {ip_dst}")

print("Firewall started... Press CTRL+C to stop.")
sniff(prn=packet_callback, store=0)
