#!/usr/bin/python
# Robert Sturzbecher 2022-10-15
# Sends an ARP packet to check if a remote LAN host is online.

# Requires scapy, by default is already installed on Kali else install with "pip install scapy" 
import sys
from scapy.all import *

def aping():
    if len(sys.argv) == 2:                                      # check if a command line paramater was supplied
        packetDest = sys.argv[1]                                # get the command line paramater, should be a IP or network address  
        answered,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=packetDest),timeout=2,verbose=True)
        for sent, received in answered:
            print(f"MAC: {received.src} \tIP: {received.psrc}" ) 
    else:
        print("Usage: ArpPing.py [Remote_IP_address or Network_address]")
        print("examples: \n\t\tArpPing.py 192.168.1.0/24 \n\t\tArpPing.py 192.168.1.1")

if __name__ == '__main__':
    print("ArpPing          Robert Sturzbecher 2022-10-15")
    aping()
