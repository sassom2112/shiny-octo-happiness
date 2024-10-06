# Port Scanner with Banner Grabbing

⚠️ Disclaimer: This tool is for educational purposes only. Unauthorized port scanning or network reconnaissance on IP addresses that you do not own or have explicit permission to scan is illegal in many jurisdictions. Always ensure you have proper authorization before conducting any security testing, including port scans, on third-party systems.

⚠️ By using this tool, you agree to abide by all local laws and regulations regarding network security and ethical hacking. Always practice responsible scanning techniques and obtain permission before testing on systems that are not your own.

#

This tool is a simple Python-based port scanner that attempts to connect to specified TCP ports on a target host. It also attempts to perform banner grabbing, which is useful for identifying the service running on a particular open port.

## Features
+ Scans specified TCP ports on a target host.
+ Attempts to grab and display the banner for open ports.
+ Provides informative output for open and closed ports.

## Requirements
`Python 3.x`

## Installation

1. Clone the repository or download the script.
2. Install the necessary dependencies, although in this case, the tool only uses Python's built-in libraries (argparse and socket)🐍:

```bash
git clone https://github.com/your-repo/port-scanner.git
cd port-scanner
```

## Running the Tool

To run the script, you need to specify the target host (-H) and the target ports (-p) separated by commas:

```bash
python port_scanner.py -H <target_host> -p <port1,port2,port3,...>
```

### Example:
```bash
python3 port_scanner.py -H scanme.nmap.org -p 80,443,22
```
💡 **Tip**: The scanme.nmap.org website is meant to allow users to test port scanning.

⚠️ **Caution**: you should only scan hosts you own or have explicit permission to scan, even if they seem publicly accessible.

```bash
[+] Scan results for: scanme.nmap.org (45.33.32.156)
[+] Scanning port 80 on 45.33.32.156
[+] 80/tcp open
[-] No banner received for 80/tcp
[+] Scanning port 443 on 45.33.32.156
[-] 443/tcp closed
[+] Scanning port 22 on 45.33.32.156
[+] 22/tcp open
[+] Banner for 22/tcp: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
```
This will scan the host scanme.nmap.org on ports 80, 443, and 22, attempting to determine if the ports are open and display any banners it receives.

### Output:
If a port is open the script will:
+ print the port number and attempt to display the service banner.

If a port is closed 
+ it will notify you.


### What We Learned 
In this project, we **opted** (pun intented) for using the `argparse` library instead of `optparse`, which has been deprecated since Python 2.7. Here are the key reasons for this choice:

⚙️ **Maintenance**: argparse is the standard library for argument parsing in Python, which means it is well-maintained and widely supported in newer Python versions.

🎯 **Ease of Use**: argparse provides a simpler and more intuitive API for handling command-line arguments, including built-in help text, argument validation, and support for required/optional arguments.

⚡ **Extensibility**: argparse can easily handle complex argument parsing scenarios with minimal code changes, making it a flexible and powerful choice.

By using argparse, we not only extended the life of the code but also simplified the process of adding additional command-line options or features to the tool in the future.
