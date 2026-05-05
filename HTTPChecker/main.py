import requests
import time
from sys import argv

def check(url, interval):
    print(f"Monitoring: {url}  (interval: {interval}s)")
    print("-" * 50)
    while True:
        try:
            result = requests.get(url, timeout=10)
            status = f"HTTP {result.status_code}"
            if result.status_code < 400:
                print(f"{time.asctime()}  ✅  {status}")
            else:
                print(f"{time.asctime()}  ⚠️  {status}")
        except requests.exceptions.ReadTimeout:
            print(f"{time.asctime()}  ❌  Timeout")
        except requests.exceptions.ConnectionError:
            print(f"{time.asctime()}  ❌  Connection failed")
        time.sleep(interval)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python main.py <url> [interval_seconds]")
        print("Example: python main.py https://google.com 60")
        exit(1)
    url = argv[1]
    interval = int(argv[2]) if len(argv) > 2 else 60
    check(url, interval)
