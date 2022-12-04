import paramiko
import time
import socket
import json
from sys import argv

switchIP = argv[1]

print(switchIP)
input()

with open ('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\logpass.pwd', 'r') as f:
    logpassJSON = f.read()

logpass = json.loads(logpassJSON)
#print(logpass[0]["login"])
client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=switchIP, username=logpass[0]["login"], password=logpass[0]["password"], look_for_keys=False, allow_agent=False)
ssh = client.invoke_shell()
ssh.send("\n")
ssh.send("sh ip int br\n")
text = ssh.recv(60000)
ssh.close()
input()
print(text)
input()



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