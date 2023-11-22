import scapy.all as scapy
from colorama import Fore


class Scanner:
    def __init__(self,range) -> None:
        self.range = range
        print(f"[+] Scanning subnet {self.range}")

    def scan(self):
        arp_header = scapy.ARP(pdst = self.range)
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
            print(f"IP\t\t\t\tMAC")
            print("-------------------------------------------------------")
            for network in networks:
                print(f"{Fore.LIGHTMAGENTA_EX if network['you']==True else ''}{network['ip']}\t\t{network['mac']}\t{f'<< [YOU]' if network['you']==True else ''}{Fore.RESET}")
            print('\n')
        else:
            print("[X] No Networks Found!!")
        
