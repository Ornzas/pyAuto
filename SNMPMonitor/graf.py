import matplotlib.pyplot as plt
import csv
from sys import argv

def plot(csv_file):
    timestamps = []
    series = {}

    with open(csv_file, "r") as f:
        for row in csv.reader(f):
            if len(row) < 2:
                continue
            timestamps.append(row[0].strip())
            for i, val in enumerate(row[1:], start=1):
                series.setdefault(i, [])
                try:
                    series[i].append(float(val.strip()))
                except ValueError:
                    series[i].append(None)

    print(f"Rows: {len(timestamps)}, Series: {len(series)}")

    for i, values in series.items():
        plt.plot(timestamps, values, label=f"Device {i}")

    plt.title("SNMP Voltage Monitor")
    plt.xlabel("Time")
    plt.ylabel("Voltage, [V]")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_file = argv[1] if len(argv) > 1 else "output.csv"
    plot(csv_file)
