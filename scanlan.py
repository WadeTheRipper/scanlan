#import nmap
import os

#getting ip address
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_addr = s.getsockname()[0]
print(ip_addr)
ip = list(ip_addr.split("."))
ip.pop()
new_ip = ".".join(ip)
final= new_ip + ".1/24"
#print(final)
os.system("nmap "+ final)
s.close()

#scan block



