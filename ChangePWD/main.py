from switch import *
from sys import argv

# input("1!!")
switchIP = argv[1]
# input("2!!")
# getLoginsFrom(fileWithLogins)
ssh = connectTo(switchIP)

# input("3!!")
commandWithoutData("terminal length 0", ssh)
# input("4!!")
for neighbor in commandWithData("show cdp neighbors detail", ssh).split("-------------------------"):
    oneSwitch = False
    # remoteSwitch = ""
    # print(remoteSwitch)
    # interface = list()
    # print(neighbor)
    #if not re.findall(r"show cdp neighbors detail",neighbor):
    for line in neighbor.split("\r\n"):
        if re.findall(r"IP address:",line) and not oneSwitch:
            remoteSwitch = line.split(":")[1].replace(" ","")
            oneSwitch = True
        if re.findall(r"Interface:",line) and re.findall(r"Port ID", line):
            interface = [line.split(",")[0].split(":")[1].replace(" ","") , line.split(",")[1].split(":")[1].replace(" ","")]
    if oneSwitch:        
        print(interface[0] + " to " + interface[1] + " sw " + remoteSwitch)
    #print(interface[0])

input('Success!')