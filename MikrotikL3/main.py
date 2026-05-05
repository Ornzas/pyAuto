import json
import time
from sys import argv
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

def load_credentials(path="logpass.pwd"):
    with open(path, "r") as f:
        creds = json.load(f)
    return creds[0]["login"], creds[0]["password"]

def load_nodes(path="nodes.conf"):
    nodes = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                nodes.append(line)
    return nodes

if __name__ == "__main__":
    creds_file = argv[1] if len(argv) > 1 else "logpass.pwd"
    username, password = load_credentials(creds_file)
    nodes = load_nodes()

    print(f"Nodes to check: {len(nodes)}")
    print("-" * 50)
    start = time.time()

    for node in nodes:
        print(f"\n[{node}]")
        try:
            conn = ConnectHandler(
                host=node,
                username=username,
                password=password,
                device_type="mikrotik_routeros"
            )
            output = conn.send_command("ip address print")
            conn.disconnect()
            print(output)
        except NetmikoTimeoutException:
            print("  ❌  Timeout — host unreachable")
        except NetmikoAuthenticationException:
            print("  ❌  Authentication failed")
        except Exception as e:
            print(f"  ❌  Error: {e}")

    print(f"\nDone in {time.time() - start:.2f}s")
