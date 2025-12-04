import socket

# Main port scanner function
def port_scanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # slightly higher timeout
        sock.connect((ipaddress, port))
        return f"[+] PORT OPEN {port}"
    except socket.error:
        return f"[-] PORT CLOSED {port}"
    finally:
        try:
            sock.close()
        except:
            pass

# Handles single or multiple target scanning
def scan(targets, ports):
    results = []

    target_list = [t.strip() for t in targets.split(',')]
    for ip in target_list:
        results.append(f"\nScanning {ip}")
        for port in range(1, ports + 1):
            results.append(port_scanner(ip, port))

    return results

# CLI testing
if __name__ == "__main__":
    targets = input("Enter target(s) to scan (split multiple targets with ','): ")
    ports = int(input("Enter number of ports to scan: "))
    scan_results = scan(targets, ports)
    for result in scan_results:
        print(result)
