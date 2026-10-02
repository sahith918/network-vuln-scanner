import nmap
from analyzer import analyze
from report import generate_report

target = input("Enter target IP: ")

scanner = nmap.PortScanner()
scanner.scan(target, '1-1000', arguments='-sV')

findings = []

for host in scanner.all_hosts():
    print(f"\nHost: {host} ({scanner[host].state()})")
    for proto in scanner[host].all_protocols():
        for port in sorted(scanner[host][proto].keys()):
            svc = scanner[host][proto][port]
            service_line = f"{svc['name']} {svc['product']} {svc['version']}".strip()
            print(f"  Port {port}/{proto}: {service_line}")

            result = analyze(port, service_line)
            if result:
                findings.append(result)

print(f"\n{len(findings)} vulnerabilities found.")
generate_report(findings, target)
