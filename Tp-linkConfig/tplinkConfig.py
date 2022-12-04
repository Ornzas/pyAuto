import time
#time.sleep(2)
with open ('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\Config.txt', 'r') as f:
    config = f.read()
#f = open('C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\Config.txt', 'r')
#config = f.read()
f.close()
#time.sleep(2)
#print(config)
#{ipGateway}
#{ipAddress} {netMask}
#time.sleep(1)
with open("C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\ipAddresses.txt", "r") as f:
    for ip in f:
        #print("dghdh")
        #input()
        #ipAddress = ip.replace("\t","")
        ipAddressArray = ip.split("\t")
        #input()
        #print(ipAddressArray)
        #input()
        #time.sleep(4)
        ipAddress = ipAddressArray[0] + ipAddressArray[1]
        ipAddress = ipAddress.replace("\n","")
        ipAddress = ipAddress.replace("\r","")
        #print("ip " + ipAddress)
        #input("dfhdhd___")
        lastOctet = int(ipAddressArray[1])
        lastOctet -= 1
        #input("dfhdhd_+_")
        gateway = ipAddressArray[0] + str(lastOctet)
        #print("gw " + gateway)
        newConfig = config.replace('{ipAddress}', ipAddress)
        newConfig = newConfig.replace('{ipGateway}', gateway)
        f = open(ipAddress + '.txt', 'w')
        for line in newConfig:
            f.write(line)
        f.close()
        #print(newConfig)

        print("new_config for ip: " + ipAddress)


        
##with open("C:\\Users\\kasatkindi\\Desktop\\Bascket\\pyAuto\\Config.txt", "r") as f:
##    for line in f:
##        #print(config + line)
##        print(line.replace('{ipGateway}', '{ipGateway__}'))

#print ("+++++++++++++++++++++++++++++++++++++")
#print (config)
#f.close()
#time.sleep(1)
input()
