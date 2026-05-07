import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, 'Config.txt'), 'r') as f:
    config = f.read()

with open(os.path.join(script_dir, 'ipAddresses.txt'), 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) < 2:
            continue
        ip_address = parts[0] + parts[1]
        gateway = parts[0] + str(int(parts[1]) - 1)
        new_config = config.replace('{ipAddress}', ip_address).replace('{ipGateway}', gateway)
        out_path = os.path.join(script_dir, ip_address + '.txt')
        with open(out_path, 'w') as out:
            out.write(new_config)
        print(f"Config generated for: {ip_address}")
