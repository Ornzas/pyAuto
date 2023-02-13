import paramiko
import time
import socket
import json
import re
import logging

max_bytes=60000
fileWithLogins = 'C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\logpass.pwd'
# fileWithLogins = '..\\logpass.pwd'

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
    
def isCOuntOfMac(line):
    return re.findall(r"^Total Mac Addresses for this criterion",line)
    
def isGreateOfOne(line):
    return int(resultCommandShMacAddressTable.split(":")[1].replace(" ","")) > 1

def getLoginsFrom(file):
    with open (file, 'r') as f:
        loginsJSON = f.read()

    return json.loads(loginsJSON)

def commandWithoutData(command, ssh):
    ssh.send(command + "\n")
    time.sleep(1.5)
    ssh.recv(max_bytes)
    return True

def commandWithData(command, ssh):
    ssh.send(command + "\n")
    time.sleep(1.5)
    #print('do commandWithData')
    #print(ssh.recv(max_bytes).decode("utf-8"))
    return ssh.recv(max_bytes).decode("utf-8")

def connectTo(switchIP):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # for login in logins:
    succeedConnection = False
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
            succeedConnection = True
            break
        except TimeoutError:
            print("Device is not recheable!")
            return False
            #exit()
        except paramiko.ssh_exception.AuthenticationException:
            print("Authentication failed user {}!".format(username))
            next
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("Unable to connect to port 22 on {}!".format(switchIP))
            next
        except AttributeError:
            print("'NoneType' object has no attribute 'open_session'")
            next
        except paramiko.ssh_exception.SSHException:
            print("Error reading SSH protocol banner")
            next
    if succeedConnection:
        print("Authentication succeed user {}!".format(username))
        try:
            return client.invoke_shell()
        except AttributeError:
            #exit()
            next
    else:
        print('Failed to connect to {}!'.format(switchIP))
        #exit()
        return False
    return True

if __name__ == '__main__':
    input("Use only in another scripts")