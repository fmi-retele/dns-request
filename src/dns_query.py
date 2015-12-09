'''
Sample script to send a DNS query 
'''
import scapy
from scapy.sendrecv import sendp, sniff, sr1
from scapy.all import  IP, UDP, DNS, DNSQR

google_DNS_service = '8.8.8.8'
name_to_find = "fmi.unibuc.ro"

network_layer = IP(dst = google_DNS_service)
transport_layer = UDP(dport = 53)
dns = DNS(rd = 1)
dns_query = DNSQR(qname = name_to_find)
dns.qd = dns_query

pachet = network_layer / transport_layer / dns

# send and recieve one packet 
answer = sr1(pachet)
print answer[DNS].summary()
