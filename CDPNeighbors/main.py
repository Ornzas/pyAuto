from switch import *
from sys import argv
import logging
import threading
import time
# CDPNeighbors\main.py 172.16.153.1  -f CDPdata\Nekrasovo14 -t
"""show cdp neighbors detail
-------------------------
Device ID: c9200-sw7.gsprom.local
Entry address(es):
  IP address: 172.16.215.201
Platform: cisco C9200L-48P-4G,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 163 sec

Version :
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_LITE_IOSXE), Version 16.9.3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 20-Mar-19 07:28 by mcpre

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 172.16.215.201

-------------------------
Device ID: c9200-sw7.gsprom.local
Entry address(es):
  IP address: 172.16.215.201
Platform: cisco C9200L-48P-4G,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/16,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 166 sec

Version :
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_LITE_IOSXE), Version 16.9.3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 20-Mar-19 07:28 by mcpre

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 172.16.215.201

-------------------------
Device ID: C4331_GSP-Servis.gsprom.local
Entry address(es):
  IP address: 172.17.8.62
Platform: cisco ISR4331/K9,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet2/0/24,  Port ID (outgoing port): GigabitEthernet0/0/0
Holdtime : 160 sec

Version :
Cisco IOS Software [Fuji], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 20-Mar-19 08:02 by mcpre

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es):
  IP address: 172.17.8.62

-------------------------
Device ID: C4331_GSP-Servis.gsprom.local
Entry address(es):
  IP address: 172.17.8.62
Platform: cisco ISR4331/K9,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/24,  Port ID (outgoing port): GigabitEthernet0/0/1
Holdtime : 158 sec

Version :
Cisco IOS Software [Fuji], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 20-Mar-19 08:02 by mcpre

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es):
  IP address: 172.17.8.62

-------------------------
Device ID: c2960_sw3-video.gsprom.local
Entry address(es):
  IP address: 172.16.215.197
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/20,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 161 sec

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
  IP address: 172.16.215.197

-------------------------
Device ID: c2960_sw3-video.gsprom.local
Entry address(es):
  IP address: 172.16.215.197
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/20,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 121 sec

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
  IP address: 172.16.215.197

-------------------------
Device ID: sw2960-spb-nekrasova14a.2.14.gsprom.loca
Entry address(es):
  IP address: 172.25.2.14
Platform: cisco WS-C2960-48TC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/17,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 154 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(53)SE1, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 12-Mar-10 17:38 by prod_rel_team

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000025B45D1B00FF0000
VTP Management Domain: 'gsprom'
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 172.25.2.14

-------------------------
Device ID: c2960_sw4.gsprom.local
Entry address(es):
  IP address: 172.16.215.198
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/21,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 159 sec

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
  IP address: 172.16.215.198

-------------------------
Device ID: c2960_sw4.gsprom.local
Entry address(es):
  IP address: 172.16.215.198
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/21,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 173 sec

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
  IP address: 172.16.215.198

-------------------------
Device ID: c2960_sw5.gsprom.local
Entry address(es):
  IP address: 172.16.215.199
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/22,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 176 sec

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
  IP address: 172.16.215.199

-------------------------
Device ID: c2960_sw5.gsprom.local
Entry address(es):
  IP address: 172.16.215.199
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/22,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 170 sec

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
  IP address: 172.16.215.199

-------------------------
Device ID: c2960_sw6.gsprom.local
Entry address(es):
  IP address: 172.16.215.200
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/23,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 124 sec

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
  IP address: 172.16.215.200

-------------------------
Device ID: c2960_sw6.gsprom.local
Entry address(es):
  IP address: 172.16.215.200
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/23,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 175 sec

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
  IP address: 172.16.215.200

-------------------------
Device ID: c2960_sw1.gsprom.local
Entry address(es):
  IP address: 172.16.215.195
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/18,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 129 sec

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
  IP address: 172.16.215.195

-------------------------
Device ID: c2960_sw1.gsprom.local
Entry address(es):
  IP address: 172.16.215.195
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/18,  Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime : 164 sec

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
  IP address: 172.16.215.195

-------------------------
Device ID: c2960_sw2.gsprom.local
Entry address(es):
  IP address: 172.16.215.196
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet2/0/19,  Port ID (outgoing port): GigabitEthernet1/0/48
Holdtime : 131 sec

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


Total cdp entries displayed : 17
c3850-core-gsp-serv#
"""

def thread_function(name):
    print("Thread %s: starting", name)
    time.sleep(2)
    print("Thread %s: finishing", name)

'''
def getCDPInfornationFrom(ip):
    #i = 1
    print('Work wiht ip {}'.format(ip))
    ssh = connectTo(ip)
    commandWithoutData("terminal length 0", ssh)
    for neighbor in commandWithData("show cdp neighbors detail", ssh).split("-------------------------"):
        oneSwitch = False
        outputString = ""
        #print('debug1')
        for line in neighbor.split("\r\n"):
            if re.findall(r"IP address:",line) and not oneSwitch:
                #print('!')
                remoteSwitch = line.split(":")[1].replace(" ","")
                oneSwitch = True
            if re.findall(r"Platform:", line):
                platform = line.split(",")[0].split(":")[1].strip()
            if re.findall(r"Interface:",line) and re.findall(r"Port ID", line):
                interface = [line.split(",")[0].split(":")[1].replace(" ","") , line.split(",")[1].split(":")[1].replace(" ","")]

            if re.findall(r"Device ID:",line):
                deviceId = line.split(",")[0].split(":")[1].replace(" ","")

        if oneSwitch:
            #print('debugsw')
            if ansibleFormat:
                print(deviceId + ":\r\nansible_host: " + remoteSwitch)
            else:
                #print(ip + " " + outputString)
                if interface[0] not in switches[ip]['interfaces']:
                    switches[ip]['interfaces'][interface[0]] = {}
                switches[ip]['interfaces'][interface[0]][remoteSwitch] = interface[1]
                #print("====" + interface[0])
                #rint(switches[ip]['interfaces'][interface[0]])
                #[interface[0]][remoteSwitch] = interface[1]
                #print(switches[ip])
                #print(interface[0] + " to " + interface[1] + " sw " + deviceId)
                #print(remoteSwitch + ", " + platform)
            if buildTree:
                if remoteSwitch in switches:
                    print("Switches have {} switch".format(remoteSwitch))
                else:
                    if platform not in excluded:
                        switches[remoteSwitch] = {}
                        switches[remoteSwitch]['interfaces'] = {}
                        switches[remoteSwitch]['platform'] = platform
                        switches[remoteSwitch]['hostname'] = deviceId
                        print("Connect to {}, {}".format(remoteSwitch, platform))
                        #i+=1
                        x = threading.Thread(target=getCDPInfornationFrom, args=(remoteSwitch,))
                        x.start()
                        x.join()
'''

def getCDPInfornationFrom(ip):
    #i = 1
    print('Work with ip {}'.format(ip))
    interfaces = {}
    ssh = connectTo(ip)
    if (ssh):
        commandWithoutData("terminal length 0", ssh)
    #    hostname = commandWithData("terminal length 0", ssh).split("\r\n")[2].split("#")[0]
    #    domain = commandWithData("sh ip domain", ssh).split("\r\n")[1]
    #    fullHostname = hostname + "." + domain
    #    if fullHostname not in switches:
    #        switches[fullHostname] = {}
    #        switches[fullHostname]['interfaces'] = {}

        for neighbor in commandWithData("show cdp neighbors detail", ssh).split("-------------------------"):
            oneSwitch = False
            outputString = ""
            for line in neighbor.split("\r\n"):
                if re.findall(r"IP address:",line) and not oneSwitch:
                    remoteSwitch = line.split(":")[1].replace(" ","")
                    oneSwitch = True
                if re.findall(r"Platform:", line):
                    platform = line.split(",")[0].split(":")[1].strip()
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
                        if platform not in excluded:
                            switches[deviceId] = {}
                            switches[deviceId]['interfaces'] = {}
                            switches[deviceId]['platform'] = platform
                            switches[deviceId]['ip'] = remoteSwitch
                            print("Connect to {}, '{}'".format(switches[deviceId]['ip'], platform))
                            #i+=1
                            switches[deviceId]['interfaces'] = getCDPInfornationFrom(remoteSwitch)
                            #x = threading.Thread(target=getCDPInfornationFrom, args=(switches[deviceId]['ip'],))
                            #x.start()
                            #x.join()
    return interfaces

    
    
    
if __name__ == "__main__":

    excluded = ['Cisco IP Phone 8841',
                'Cisco IP Phone 8851',
                'Cisco IP Phone 7821',
                'Cisco IP Phone 8861',
                'Cisco IP Phone 8865',
                'Cisco IP Phone 7911',
                'Cisco IP Phone 7841',
                'Cisco IP Phone 7941',
                'Cisco IP Phone 7960',
                'Cisco IP Phone 8845',
                'Cisco IP Phone 6921',
                'Cisco IP Phone 7962',
                'Cisco IP Phone 8832',
                'Cisco IP Phone 7942',
                'Cisco IP Phone 6945',
                'CTS-CODEC-inTouch',
                'CTS-CODEC-SX20',
                'Codec Plus',
                'NanoBeam 5AC Gen2',
                'NanoBeam 5AC Gen2',
                'airFiber 5U',
                'cisco AIR-AP1815I-R-K9',
                'NanoStation loco M5',
                'NanoStation M2',
                'NanoStation M5',
                'Rocket M2',
                'Cisco IP Phone 3905',
                'CISCO ATA SPA112',
                'Rocket M5',
                'NanoStation loco M2',
                'MikroTik',
                'cisco AIR-CAP3702I-R-K9',
                'PowerBeam M5 400',
                'Rocket Prism 5AC Gen2',
                'Cisco SG200-18 (PID',
                'NS2',
                'Bullet M5',
                'AIR-CT5508-K9',
                'CTS-CODEC-SX80',
                'Cisco IP Phone 9971',
                'Cisco IP Phone 8831',
                'cisco AIR-AP2802I-R-K9']
                
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
    Full = getCDPInfornationFrom(switchIP)
    if outFile:
        file = open(outFile + '.json', 'w')
        file.write(json.dumps(switches))
        file.close()
    else:
        print(switches)
    input('Success!')