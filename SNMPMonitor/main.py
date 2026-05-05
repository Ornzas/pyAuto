import json
import time
from sys import argv
from pysnmp.hlapi import *

def load_devices(path="devices.conf"):
    with open(path, "r") as f:
        return json.load(f)

def poll(device):
    result = next(getCmd(
        SnmpEngine(),
        CommunityData(device["community"], mpModel=0),
        UdpTransportTarget((device["name"], 161), timeout=2, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity(device["oid"]))
    ))
    errorIndication, errorStatus, errorIndex, varBinds = result
    if errorIndication:
        return None, str(errorIndication)
    if errorStatus:
        return None, errorStatus.prettyPrint()
    raw = int(varBinds[0][1])
    return raw / device.get("scale", 1), None

if __name__ == "__main__":
    devices_file = argv[1] if len(argv) > 1 else "devices.conf"
    output_file  = argv[2] if len(argv) > 2 else "output.csv"
    interval     = int(argv[3]) if len(argv) > 3 else 10

    devices = load_devices(devices_file)
    print(f"Monitoring {len(devices)} device(s) → {output_file}  (interval: {interval}s)")
    print("-" * 50)

    while True:
        row = [time.asctime()]
        parts = []
        for dev in devices:
            value, err = poll(dev)
            if err:
                parts.append(f"{dev['label']}: ERR({err})")
                row.append("ERR")
            else:
                parts.append(f"{dev['label']}: {value:.2f}V")
                row.append(str(value))
        print(", ".join(parts))
        with open(output_file, "a") as f:
            f.write(", ".join(row) + "\n")
        time.sleep(interval)
