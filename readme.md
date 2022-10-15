**ArpPing**
A simple python script that scans an IP address or network address using ARP requests to find online hosts

Requires scapy installed (can install with "pip install scapy")
Scapy comes pre installed in Kali, scapy now supports Windows 

Note: 
1. root access is required for raw port access. 
2. ARP is a non routable protocol so will only work for local network addresses. 


**Example usage:**

To scan a network address 
python ArpPing 192.168.1.0/24

To scan a single IP address
python ArpPing 192.168.1.1

![Screenshot](https://github.com/GR0B/ArpPing/blob/main/screenshot.png)
