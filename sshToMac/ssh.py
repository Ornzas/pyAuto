import paramiko
import time
import socket
import json
import re
from sys import argv

def isTrunk(port):
    """Описание функции isTrunk()
    Функция возвращает True если тип порта транк"""
    if ports[port]["type"] == "trunk":
        return True
    return False

def isNotTrunk(port):
    """Описание функции isNotTrunk()
    Функция возвращает True если тип порта не транк"""
    if ports[port]["type"] != "trunk":
        return True
    return False
    
def isConnected(port):
    """Описание функции isConnected()
    Функция возвращает True порт подключен"""
    if ports[port]["state"] == "connected":
        return True
    return False
    
def isCountOfMac(line):
    return re.findall(r"^Total Mac Addresses for this criterion",line)
    
def isGreateOfOne(line):
    return int(line.split(":")[1].replace(" ","")) > 1

def getLoginsFrom(file):
    with open (file, 'r') as f:
        loginsJSON = f.read()

    return json.loads(loginsJSON)

def commandWithoutData(command):
    ssh.send(command + "\n")
    time.sleep(0.5)
    ssh.recv(max_bytes)
    return True

def commandWithData(command):
    ssh.send(command + "\n")
    time.sleep(0.5)
    return ssh.recv(max_bytes).decode("utf-8")

switchIP = argv[1]
max_bytes=60000
fileWithLogins = '..\\logpass.pwd'
# logins = getLoginAndPassword('..\\logpass.pwd')
# input("forLogins")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# for login in logins:
for login in getLoginsFrom(fileWithLogins):
    username = login["login"]
    password = login["password"]
    try:
        client.connect(
            hostname = switchIP,
            username = username,
            password = password,
            look_for_keys = False,
            allow_agent = False,
        )
        break
    except TimeoutError:
        input("Device is not recheable!")
        exit()
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed user {}!".format(username))
        next

print("Authentication succeed user {}!".format(username))
ssh = client.invoke_shell()

commandWithoutData("terminal length 0")

ports = {}
for line in commandWithData("show interfaces status").split("\r\n"):
    # if line != '' and line != 'sh interfaces status' and line.find("Port") < 0 and line[42:53].replace(" ","") != "":
    typeOfPort = line[42:53].replace(" ","")
    # if line[42:53].replace(" ","") != "":
    if typeOfPort :
        """
        line[0:9].replace(" ","") - интерфейс/порт
        line[10:29] - discription, как подписан порт
        line[29:42].replace(" ","") - состояние
        line[42:53].replace(" ","")) - тип порта или нативный влан.
        """
        port = line[0:9].replace(" ","")
        stateOfPort = line[29:42].replace(" ","")
        nameOfPort = line[10:29]
        ports[port] = {
                        "type" : typeOfPort ,
                        "state" : stateOfPort ,
                        "name" : nameOfPort
                      }

# input("!")

for port in ports:
    """Выбираем только подключенные и не транковые порты"""
    # input(port)
    if isConnected(port) and isNotTrunk(port):
        # input("True and True")
        for resultCommandShMacAddressTable in commandWithData("show mac address-table interface {}\n".format(port)).split("\r\n"):
            # input("Count")
            if isCountOfMac(resultCommandShMacAddressTable) and isGreateOfOne(resultCommandShMacAddressTable):
                print("Port {} has {} MAC\'s".format(port, resultCommandShMacAddressTable.split(":")[1].replace(" ","")))

"""Ждем ввод пользователя, с сообщением об удачном завершении скрипта, актуально для винды тк она торопится закрыть окно со скриптом"""
input('Success!')