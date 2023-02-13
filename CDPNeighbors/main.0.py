from switch import *
from sys import argv

"""
Device ID: c2960_sw2.gsprom.local
Entry address(es):
  IP address: 172.16.215.196
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/19,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 152 sec

Version :
Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(4)E8, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Fri 15-Mar-19 10:55 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 172.16.215.196
"""

switchIP = argv[1]
showDeviceId = ""
ansibleFormat = ""
# input("2!!")
# getLoginsFrom(fileWithLogins)
ssh = connectTo(switchIP)
excluded = ['Cisco IP Phone 8841',
            'Cisco IP Phone 8851',
            'Cisco IP Phone 7821',
            'Cisco IP Phone 8861',
            'Cisco IP Phone 8865',
            'Cisco IP Phone 7911']
# input("3!!")
commandWithoutData("terminal length 0", ssh)
# input("4!!")
for neighbor in commandWithData("show cdp neighbors detail", ssh).split("-------------------------"):
    oneSwitch = False
    outputString = ""
    # remoteSwitch = ""
    # print(remoteSwitch)
    # interface = list()
    # print(neighbor)
    #if not re.findall(r"show cdp neighbors detail",neighbor):
    for line in neighbor.split("\r\n"):
        if re.findall(r"IP address:",line) and not oneSwitch:
            remoteSwitch = line.split(":")[1].replace(" ","")
            outputString += " sw " + remoteSwitch
            oneSwitch = True
        if re.findall(r"Platform:", line):
            platform = line.split(",")[0].split(":")[1].strip()
        #Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP

        if re.findall(r"Interface:",line) and re.findall(r"Port ID", line):
            interface = [line.split(",")[0].split(":")[1].replace(" ","") , line.split(",")[1].split(":")[1].replace(" ","")]
            outputString = interface[0] + " to " + interface[1] + outputString
        if showDeviceId:
            # print("EEe2")
            if re.findall(r"Device ID:",line):
                # print("EEe3")
                deviceId = line.split(",")[0].split(":")[1].replace(" ","")
                outputString = outputString + " " + deviceId
#                    c2960_sw4.gsprom.local:
#                    ansible_host: 172.16.215.198

    if oneSwitch:
        if ansibleFormat:
            print(deviceId + ":\r\nansible_host: " + remoteSwitch)
        else:
            print(outputString)
        print(platform)
        if platform not in excluded:
            print('НЕ ТЕЛЕФОН')
    #print(interface[0])

input('Success!')
