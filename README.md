# pyAuto

Python network automation toolkit developed for real-world infrastructure management.

## Tools

| Tool | Description |
|------|-------------|
| [CDPNeighbors](#cdpneighbors) | Recursive CDP network discovery → JSON / Ansible inventory |
| [VisualisationCDP](#visualisationcdp) | Interactive HTML topology graph from CDPNeighbors output |
| [HTTPChecker](#httpchecker) | Generic HTTP/HTTPS availability monitor |
| [MikrotikL3](#mikrotikl3) | Collect IP address info from MikroTik devices via SSH |
| [SNMPMonitor](#snmpmonitor) | DC voltage monitoring via SNMP — MikroTik + SNR ERD |
| [Tp-linkConfig](#tp-linkconfig) | Bulk TP-Link config generation from template |

## Prerequisites

```
pip install netmiko pysnmp pyvis matplotlib requests paramiko
```

## Credentials

Tools that connect to devices use `logpass.pwd`:

```
cp logpass.pwd.sample logpass.pwd
# edit with your credentials
```

---

## CDPNeighbors

Recursively discovers network topology via CDP over SSH. Starting from a seed
device, walks the network collecting hostnames, IPs, platforms, and serial
numbers. Exports to JSON and optionally generates an Ansible inventory.

```
python CDPNeighbors/main.py <seed_ip> [-t] [-f <output_name>]
```

| Flag | Description |
|------|-------------|
| `-t` | Enable recursive traversal |
| `-f <name>` | Save output to `<name>.json` |

```
python CDPNeighbors/main.py 192.168.1.1 -t -f topology
```

---

## VisualisationCDP

Reads JSON from CDPNeighbors and renders an interactive HTML graph (pyvis).
Nodes are color-coded by platform; hover shows serial numbers and interfaces.

```
python VisualisationCDP/main.py <json_name>
```

Typical workflow:

```
python CDPNeighbors/main.py 192.168.1.1 -t -f site
python VisualisationCDP/main.py site
```

---

## HTTPChecker

Monitors an HTTP/HTTPS endpoint at a given interval. Prints timestamped
status with HTTP code; warns on 4xx/5xx.

```
python HTTPChecker/main.py <url> [interval_seconds]
python HTTPChecker/main.py https://example.com 60
```

---

## MikrotikL3

Connects to a list of MikroTik devices via SSH and runs `ip address print`
on each. Device list is read from `nodes.conf` (lines with `#` are skipped).

```
cp MikrotikL3/nodes.conf.sample MikrotikL3/nodes.conf
python MikrotikL3/main.py [logpass.pwd]
```

> Work in progress — SSH output parsing may vary by RouterOS version.

---

## SNMPMonitor

Monitors DC voltage on remote sites via SNMP. Polls MikroTik device voltage
and SNR ERD input voltage simultaneously, allowing comparison of supply
voltage vs voltage at the device. Results are saved to CSV; graf.py builds
a time-series plot.

```
cp SNMPMonitor/devices.conf.sample SNMPMonitor/devices.conf
python SNMPMonitor/main.py [devices.conf] [output.csv] [interval_seconds]
python SNMPMonitor/graf.py [output.csv]
```

---

## Tp-linkConfig

Generates individual configuration files for TP-Link devices from a shared
template. Replaces `{ipAddress}` and `{ipGateway}` placeholders for each
device in the list — no manual editing per device needed.

Input: `Config.txt` (template) + `ipAddresses.txt` (tab-separated IP list).

```
python Tp-linkConfig/tplinkConfig.py
```

> Update file paths in the script to match your environment.
