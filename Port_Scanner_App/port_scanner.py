import socket



#Main Port scanner function that performs the scan
def port_scanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ipaddress, port))
        return f"[+] PORT OPEN {port}"
    except:
        return f"[-] PORT CLOSED {port}"
    finally:
        sock.close()

"""
Function that handles either to perform a single scan or multiple scan depending on the number 
of targets provided
"""
def scan(targets, ports):
    results = []  #this list stores the results of the scan and returns it all at once 

    # Multiple targets scan
    if ',' in targets:
        for ip in targets.split(','):
            ip = ip.strip()
            results.append(f"\nScanning {ip}")
            for port in range(1, ports + 1):
                results.append(port_scanner(ip, port))
        return results
    




    #NB:This is an else block

    # Single target scan
    results.append(f"\nScanning {targets}")
    for port in range(1, ports + 1):
        results.append(port_scanner(targets, port))

    return results




if __name__ =="main":
    targets = input("Enter target(s) to scan (split multiple targets with ','): ")
    ports = int(input("Enter number of ports to scan: "))
    scan_results = scan(targets, ports)
    for result in scan_results:
        print(result)