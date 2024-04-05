import scapy.all as scapy

# 1) arp request
# 2) broadcast
# 3) response

# 1
arp_request_packet = scapy.ARP(pdst="192.168.0.1/24")
# scapy.ls(scapy.ARP())

# 2
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# scapy.ls(scapy.Ether())


combined_packet = broadcast_packet/arp_request_packet
result = scapy.srp(combined_packet)
print(result)