import argparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        # Create a socket object
        connSkt = socket(AF_INET, SOCK_STREAM)
        # Connect to the host and port
        connSkt.connect((tgtHost, tgtPort))
        # Set a timeout for receiving the banner (optional)
        connSkt.settimeout(2)

        # Print open port message
        print(f"[+] {tgtPort}/tcp open")

        # Try to receive the banner (banner grabbing)
        try:
            # Receive up to 1024 bytes
            banner = connSkt.recv(1024).decode().strip()
            if banner:
                print(f"[+] Banner for {tgtPort}/tcp: {banner}")
            else:
                print(f"[-] No banner for {tgtPort}/tcp")
        except:
            print(f"[-] No banner received for {tgtPort}/tcp")

        connSkt.close()

    except:
        print(f"[-] {tgtPort}/tcp closed")


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve '{tgtHost}': Unknown host")
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"[+] Scan results for: {tgtName[0]} ({tgtIP})")
    except:
        print(f"[+] Scan results for: {tgtIP}")

    setdefaulttimeout(1)

    # Scanning each port
    for tgtPort in tgtPorts:
        print(f"[+] Scanning port {tgtPort} on {tgtIP}")
        connScan(tgtHost, int(tgtPort))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple port scanner with banner grabbing")
    parser.add_argument('-H', dest='tgtHost', type=str, required=True, help='Specify target host')
    parser.add_argument('-p', dest='tgtPorts', type=str, required=True, help='Specify target ports (comma-separated)')

    args = parser.parse_args()

    tgtHost = args.tgtHost
    tgtPorts = list(map(int, args.tgtPorts.split(',')))

    portScan(tgtHost, tgtPorts)

