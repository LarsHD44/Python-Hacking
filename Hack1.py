banner = "FreeFloat FTP Server"
port = 21
print("[+] Checking for "+banner+" on Port "+str(port))
portList=[21,22,25,80,110]
portOpen = True
pos = portList.index(80)
print("[+] There are "+str(pos)+" Ports to scan before 80.")
cnt = len(portList)
print("Scanning "+str(cnt)+" Total Ports.")
services = {'FTP':21,'SSH':22,'SMTP':25,'HTTP':80}
print(services.keys())
print(" ")
print(services.items())
print(" ")
print("[+] Found vuln with FTP on Port "+str(services['FTP']))
print(" ")
print(" ")
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.0.21",22))
banner = s.recv(1024)
print(banner)
