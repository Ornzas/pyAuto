import matplotlib.pyplot as plt
import csv
from sys import argv

def plot(csv_file):
    timestamps = []
    series = {}
    labels = {}

    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        # optional header row: if first cell is not a timestamp, treat as labels
        first_row = next(reader, None)
        if first_row and first_row[0].strip().startswith("#"):
            for i, lbl in enumerate(first_row[1:], start=1):
                labels[i] = lbl.strip()
            first_row = None

        for row in ([first_row] if first_row else []) + list(reader):
            if not row or len(row) < 2:
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
        lbl = labels.get(i, f"Device {i}")
        plt.plot(timestamps, values, label=lbl)

    plt.title("DC Voltage Monitor")
    plt.xlabel("Time")
    plt.ylabel("DC Voltage, [V]")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_file = argv[1] if len(argv) > 1 else "output.csv"
    plot(csv_file)
