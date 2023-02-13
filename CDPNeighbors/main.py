from switch import *
from sys import argv
import logging
import threading
import time
# CDPNeighbors\main.py 172.16.153.1  -f CDPdata\Nekrasovo14 -t
"""
-------------------------
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

def getCDPInfornationFrom(ip, externalDeviceId):
    print('Work with ip {}'.format(ip))
    interfaces = {}
    ssh = connectTo(ip)
    if (ssh):
        commandWithoutData("terminal length 0", ssh)
        
        '''
        sw-c92-spb-nekrasova14-lab.3.122#show version | i System Serial Number
System Serial Number               : JAE24070DSB
sw-c92-spb-nekrasova14-lab.3.122#show version | i Motherboard Serial Number
        '''
        systemSerialNumbers = []
        motherboardSerialNumbers = []
        for line in commandWithData("show version | i System Serial Number", ssh).split("\r\n"):
            if re.findall(r"System Serial Number\s+",line):
                systemSerialNumbers.append(line.split(":")[1].replace(" ",""))
        for line in commandWithData("show version | i System serial number", ssh).split("\r\n"):
            if re.findall(r"System serial number\s+",line):
                systemSerialNumbers.append(line.split(":")[1].replace(" ",""))
        
        for line in commandWithData("show version | i Motherboard Serial Number", ssh).split("\r\n"):
            if re.findall(r"Motherboard Serial Number\s+",line):
                motherboardSerialNumbers.append(line.split(":")[1].replace(" ",""))
        for line in commandWithData("show version | i Motherboard serial number", ssh).split("\r\n"):
            if re.findall(r"Motherboard serial number\s+",line):
                motherboardSerialNumbers.append(line.split(":")[1].replace(" ",""))
        
        for neighbor in commandWithData("show cdp neighbors detail", ssh).split("-------------------------"):
            oneSwitch = False
            outputString = ""
            for line in neighbor.split("\r\n"):
                if re.findall(r"IP address:",line) and not oneSwitch:
                    remoteSwitch = line.split(":")[1].replace(" ","")
                    oneSwitch = True
                if re.findall(r"Platform:", line):
                    [platform, features] = [line.split(",")[0].split(":")[1].strip(), line.split(",")[1].split(" ")]
                if re.findall(r"Interface:",line) :
                    if re.findall(r"Port ID", line):
                        interface = [line.split(",")[0].split(":")[1].replace(" ","") , line.split(",")[1].split(":")[1].replace(" ","")]
                    else:
                        interface = [line.split(",")[0].split(":")[1].replace(" ","") , ""]
                    

                if re.findall(r"Device ID:",line):
                    deviceId = line.split(",")[0].split(":")[1].replace(" ","")

            if oneSwitch:
                if ansibleFormat:
                    print(deviceId + ":\r\nansible_host: " + remoteSwitch)
                else:
                    if interface[0] not in interfaces:
                        interfaces[interface[0]] = {}
                    interfaces[interface[0]][deviceId] = interface[1]
                if buildTree:
                    if deviceId in switches:
                        print("Switches have {} switch".format(deviceId))
                    else:
                        if "Switch" in features:
                            switches[deviceId] = {}
                            switches[deviceId]['interfaces'] = {}
                            switches[deviceId]['platform'] = platform
                            switches[deviceId]['ip'] = remoteSwitch
                            print("Connect to {}, '{}'".format(switches[deviceId]['ip'], platform))
                            switches[deviceId]['interfaces'] = getCDPInfornationFrom(remoteSwitch, deviceId)
    if externalDeviceId != "":
        switches[externalDeviceId]['systemSerialNumbers'] = []
        switches[externalDeviceId]['systemSerialNumbers'] = systemSerialNumbers
        switches[externalDeviceId]['motherboardSerialNumbers'] = []
        switches[externalDeviceId]['motherboardSerialNumbers'] = motherboardSerialNumbers
        return interfaces

    
    
    
if __name__ == "__main__":
    switches = {}
    showDeviceId = buildTree = ansibleFormat = False
    #ansibleFormat = False
    threads = list()
    par = 0
    outFile = ""
    for parameter in argv:
        # print("!!")
        par += 1
        if parameter == "-i":
            # print("EEe")
            showDeviceId = True
#        if parameter == "-f":
#            ansibleFormat = True
        if parameter == "-t":
            buildTree = True
        if parameter == "-f":
            outFile = argv[ par ]
            

    switchIP = argv[1]
    Full = getCDPInfornationFrom(switchIP,'')
    if outFile:
        file = open(outFile + '.json', 'w')
        file.write(json.dumps(switches))
        file.close()
    else:
        print(switches)
    input('Success!')