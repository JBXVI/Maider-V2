import scapy.all as scapy
from colorama import Fore
import socket,psutil


class InterfaceScanner:
    def __init__(self,interface) -> None:
        self.interface = interface
        print(f"[+] Scanning Interface {self.interface}")

    def get_ip_address_subnet(self,interface):
        try:
            addresses = psutil.net_if_addrs()[interface]
            for addr in addresses:
                if addr.family == socket.AF_INET:
                    ip_address = addr.address
                    subnet = f"{ip_address[:ip_address.rindex('.')]}.0/24"
                    return subnet
                
        except KeyError:
            return "Interface not found"

    def scan(self):
        subnet = self.get_ip_address_subnet(self.interface)
        arp_header = scapy.ARP(pdst = subnet)
        ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_packet = ether_header/arp_header
        answered_list= scapy.srp(arp_request_packet,timeout=1,verbose=False)[0]
        networks =[]
	
        
        for elements in answered_list:
            if(len(networks)==0 and elements[1].pdst != "0.0.0.0"):
                networks.append({"ip":elements[1].pdst,"mac":elements[1].hwdst,"you":True})
            networks.append({"ip":elements[1].psrc,"mac":elements[1].hwsrc,"you":False})
        
        if(len(networks)>0):
            print("\n-------------------------------------------------------")    
            print(f"IP\t\t\t  MAC Address")
            print("-------------------------------------------------------")
            for network in networks:
                print(f"{Fore.LIGHTMAGENTA_EX if network['you']==True else ''}{network['ip']}\t\t{network['mac']}\t{f'<< [YOU]' if network['you']==True else ''}{Fore.RESET}")
            print("\n\n")
        else:
            print("[X] No Networks Found!!")
