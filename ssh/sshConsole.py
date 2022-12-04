import paramiko
import re
import time
import json
#import socket
#from pprint import pprint

max_bytes=60000
short_pause=1
long_pause=5

with open ('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\logpass.pwd', 'r') as f:
    logpassJSON = f.read()
    logpass = json.loads(logpassJSON)

while True:
    #time.sleep(0.5)
    #commands = input()
    #print(commands)
    #global mode
    waitAction = input("Input IP switch or \"q\" for exit: ")
    if waitAction == "q":
        break
    #if re.findall(r'[0-2]\d{2}\.[0-2]\d{2}\.[0-2]\d{2}\.[0-2]\d{2}', waitAction) :
    if re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', waitAction) :
        #manage mode
        ipAddress = waitAction
        cl = paramiko.SSHClient()
        cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            cl.connect(
                hostname = ipAddress,
                username = logpass[0]["login"],
                password = logpass[0]["password"],
                look_for_keys = False,
                allow_agent = False,
            )
            ssh = cl.invoke_shell()
            print(ssh.recv(max_bytes).decode("utf-8"), end = '')
            #172.17.8.85
            while True:
                #print(ssh.recv(max_bytes).decode("utf-8"), end = '')
                #command = input(ssh.recv(max_bytes).decode("utf-8"))
                command = input()
                out = ssh.send(command+"\n")
                time.sleep(0.5)
                print(ssh.recv(max_bytes).decode("utf-8"), end = '')
        except TimeoutError:
            print("Device is not recheable!")
        except paramiko.ssh_exception.AuthenticationException:
            print("Authentication failed!")
        except OSError:
            print("You're leaving connection!")

        #print(waitAction)
    
    
    
