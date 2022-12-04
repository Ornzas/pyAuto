import paramiko
import time
import socket
import json
import re
from sys import argv

max_bytes=60000
switchIP = argv[1]

with open ('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\logpass.pwd', 'r') as f:
    logpassJSON = f.read()

logpass = json.loads(logpassJSON)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=switchIP, username=logpass[0]["login"], password=logpass[0]["password"], look_for_keys=False, allow_agent=False)
ssh = client.invoke_shell()

ssh.send("terminal length 0\n")
time.sleep(0.5)
ssh.recv(max_bytes)
ssh.send("show interfaces status\n")
time.sleep(0.5)

commandRAW = ""
commandRAW = ssh.recv(max_bytes)
command = commandRAW.decode("utf-8").split("\r\n")
ports = {}
for line in command:
    if line != '' and line != 'sh interfaces status' and line.find("Port") < 0 and line[42:53].replace(" ","") != "":
        # print(line[0:9].replace(" ","") + " --" + line[10:29] + " -+ " + line[29:42].replace(" ","") + " ++ " + line[42:53].replace(" ",""))
        port = {"type":line[42:53].replace(" ",""),"state":line[29:42].replace(" ",""),"name":line[10:29]}
        ports[line[0:9].replace(" ","")] = port 

for port in ports:
    if ports[port]["state"] == "connected" and ports[port]["type"] != "trunk":
        ssh.send("show mac address-table interface {}\n".format(port))
        time.sleep(0.5)
        for lineCommandShMacAddressTable in ssh.recv(max_bytes).decode("utf-8").split("\r\n"):
            if re.findall(r"^Total Mac Addresses for this criterion",lineCommandShMacAddressTable) and int(lineCommandShMacAddressTable.split(":")[1].replace(" ","")) > 1:
                print("Port {} has {} MAC\'s".format(port, lineCommandShMacAddressTable.split(":")[1].replace(" ","")))

input('Success')