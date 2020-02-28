port = 21
banner = "FreeFloat FTP Server"
print("[+] Checking for "+banner+" on port "+str(port))
portList = [21,22,25,80,110]
print("[+] Port-List: "+str(portList))
pos = portList.index(80)
print("[+] There are "+str(pos)+" ports to scan before 80.")
cnt = len(portList)
print("[+] Scanning "+str(cnt)+" Total Ports.")
