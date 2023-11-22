import argparse,re,os

from colorama import Fore
from Tools import Listener,Logo,subnet,InterfaceScan


class Main:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('choice',choices=["spoof","backdoor","dos","scan","jam","build",'exploit'])
        parser.add_argument('-t','--type',required=True,help="attack type")
        parser.add_argument('--lhost',help="Host Ip Address")
        parser.add_argument('--lport',type=int,help='Port Number')
        parser.add_argument('--range',help="subnet range")
        parser.add_argument('--interface',help="interface")
        parser.add_argument('--mac',help="mac address")
        parser.add_argument('--target',help="targget ip address")
        parser.add_argument('--targetmac',help="targget MAC address")
        parser.add_argument('--port',help="target port")
        
        self.args = parser.parse_args()

    def forward(self):
        os.system("clear")
        choice = self.args.choice
        _type = (self.args.type).lower()
        lhost = self.args.lhost
        lport = self.args.lport
        subnet_range = self.args.range
        interface = self.args.interface
        newMac = self.args.mac
        target = self.args.target
        target_mac = self.args.targetmac
        tport = self.args.port

        Logo.Logo().logo1()
        if(choice == "backdoor"):
            if(_type =="listen"):
                ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
                if(re.match(ip_regex,lhost)):
                    try:
                        Listener.Listener(host=lhost,port=lport).listener()
                    except KeyboardInterrupt:
                        print("\nExiting..")
        elif(choice == "scan"):
            if(_type == "subnet"):
                if(subnet_range):
                    subnet.Scanner(range=subnet_range).scan()
                elif(interface):
                    InterfaceScan.InterfaceScanner(interface=interface).scan()

        elif(choice == "spoof"):
            if(_type == "mac"):
                if(newMac and interface):
                    macchanger.Macchanger(interface=interface,newMac=newMac).changeMac()
            if(_type == "arp"):
                if(interface and target ):
                    arpspoof.ArpSpoof(interface=interface,targetIP=target,targetMAC=None,gatewayMAC=None,gatewayIP=None).spoof()

        elif(choice=='exploit'):
            if(_type == "vsftpd"):
                if(tport and target):
                    vsftpd.Vsftpd(ip=target, port=tport).run()





runner = Main()
try:
    runner.forward()
except PermissionError:
    print(f"{Fore.RED}[X] Root permission Required !!{Fore.RESET}")

