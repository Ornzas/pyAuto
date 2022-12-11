import paramiko
import time
import socket
import json
import re
from sys import argv

def isTrunk(portType):
    """Описание функции isTrunk()
    Функция возвращает True если тип порта транк"""
    if portType == "trunk":
        return True
    return False

def isNotTrunk(portType):
    """Описание функции isNotTrunk()
    Функция возвращает True если тип порта не транк"""
    if portType != "trunk":
        return True
    return False
    
def isConnected(portState):
    """Описание функции isConnected()
    Функция возвращает True порт подключен"""
    if portState == "connected":
        return True
    return False

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
        """
        line[0:9].replace(" ","") - интерфейс/порт
        line[10:29] - discription, как подписан порт
        line[29:42].replace(" ","") - состояние
        line[42:53].replace(" ","")) - тип порта или нативный влан.
        """
        port = {"type":line[42:53].replace(" ",""),"state":line[29:42].replace(" ",""),"name":line[10:29]}
        ports[line[0:9].replace(" ","")] = port 

# input("!")

for port in ports:
    """Выбираем только подключенные и не транковые порты"""
    if isConnected(ports[port]["state"]) and isNotTrunk(ports[port]["type"]):
        ssh.send("show mac address-table interface {}\n".format(port))
        # print("+\n")
        time.sleep(0.5)
        for resultCommandShMacAddressTable in ssh.recv(max_bytes).decode("utf-8").split("\r\n"):
            if re.findall(r"^Total Mac Addresses for this criterion",resultCommandShMacAddressTable) and int(resultCommandShMacAddressTable.split(":")[1].replace(" ","")) > 1:
                print("Port {} has {} MAC\'s".format(port, resultCommandShMacAddressTable.split(":")[1].replace(" ","")))

"""Ждем ввод пользователя, с сообщением об удачном завершении скрипта, актуально для винды тк она торопится закрыть окно со скриптом"""
input('Success')