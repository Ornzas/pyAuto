import paramiko
import time
import socket
import json
import re
from sys import argv

max_bytes=60000
switchIP = argv[1]

# input('ONE')
with open ('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\logpass.pwd', 'r') as f:
    logpassJSON = f.read()

logpass = json.loads(logpassJSON)
# print(logpass[0]["login"])
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=switchIP, username=logpass[0]["login"], password=logpass[0]["password"], look_for_keys=False, allow_agent=False)
ssh = client.invoke_shell()

ssh.send("terminal length 0\n")
time.sleep(0.5)
ssh.recv(max_bytes)
# #.decode("utf-8")

ssh.send("show interfaces status\n")
time.sleep(0.5)
# #inrefacesRAW = ssh.recv(max_bytes).decode("utf-8")


commandRAW = ""
# # 
commandRAW = ssh.recv(max_bytes)
# #.decode("utf-8")
# # input('TWO')
# # print(commandRAW)
# input('TREE')
command = commandRAW.decode("utf-8").split("\r\n")
# input('TREE')
ports = {}
for line in command:
    if line != '' and line != 'sh interfaces status' and line.find("Port") < 0 and line[42:53].replace(" ","") != "":
        # print(line[0:9].replace(" ","") + " --" + line[10:29] + " -+ " + line[29:42].replace(" ","") + " ++ " + line[42:53].replace(" ",""))
        # print(line)
        port = {"type":line[42:53].replace(" ",""),"state":line[29:42].replace(" ",""),"name":line[10:29]}
        ports[line[0:9].replace(" ","")] = port 

# print(ports )
for port in ports:
    # print(port)
    # print("!!!")
    if ports[port]["state"] == "connected" and ports[port]["type"] != "trunk":
        # print(ports[port]["type"])
        ssh.send("show mac address-table interface {}\n".format(port))
        time.sleep(0.5)
        for lineCommandShMacAddressTable in ssh.recv(max_bytes).decode("utf-8").split("\r\n"):
            if re.findall(r"^Total Mac Addresses for this criterion",lineCommandShMacAddressTable) and int(lineCommandShMacAddressTable.split(":")[1].replace(" ","")) > 1:
                print("Port {} has {} MAC\'s".format(port, lineCommandShMacAddressTable.split(":")[1].replace(" ","")))
                # print(lineCommandShMacAddressTable.split(":")[1].replace(" ",""))

input('Success')

# ssh.send("show cdp neighbors detail\n")
# time.sleep(1)
# text = ssh.recv(max_bytes).decode("utf-8")

# print(text)
# ssh.close()
# input('TWO')

# input('TREE')

# ports = {}
# ports['Gi2/0/15']= port
# port = {"type":"15","link":"a-full/a-1000","name":"print"}
# ports['Gi2/0/16']= port
# ports
# {'Gi2/0/15': {'type': 'trunk', 'link': 'a-full/a-1000', 'name': 'print'}, 'Gi2/0/16': {'type': '15', 'link': 'a-full/a-1000', 'name': 'print'}}


# def send_show_command(
    # ip,
    # username,
    # password,
    # enable,
    # command,

# ):
    # cl = paramiko.SSHClient()
    # cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # cl.connect(
        # hostname=ip,
        # username=username,
        # password=password,
        # look_for_keys=False,
        # allow_agent=False,
    # )
    # with cl.invoke_shell() as ssh:
        # #ssh.send("enable\n")
        # #ssh.send(f"{enable}\n")
        # time.sleep(short_pause)
        # ssh.send("terminal length 0\n")
        # time.sleep(short_pause)
        # ssh.recv(max_bytes)

        # result = {}
        # for command in commands:
            # ssh.send(f"{command}\n")
            # ssh.settimeout(5)

            # output = ""
            # while True:
                # try:
                    # part = ssh.recv(max_bytes).decode("utf-8")
                    # output += part
                    # time.sleep(0.5)
                # except socket.timeout:
                    # break
            # result[command] = output

        # return result


#if __name__ == "__main__":
    #ipAddress = input()
    #devices = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    #commands = ["sh clock", "sh ip arp"]
    #result = send_show_command(ipAddress, "admin", "sxdc.1029!", "cisco", commands)
    #pprint(result, width=120)
    #input()