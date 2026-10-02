# Known vulnerable service/version signatures
VULN_DB = {
    "vsftpd 2.3.4": {"cve": "CVE-2011-2523", "desc": "Backdoor command execution", "severity": "Critical"},
    "OpenSSH 4.7": {"cve": "CVE-2008-5161", "desc": "Weak encryption / outdated SSH", "severity": "Medium"},
    "Apache httpd 2.2.8": {"cve": "Multiple", "desc": "Outdated Apache, several known CVEs", "severity": "High"},
    "Samba smbd 3.X": {"cve": "CVE-2007-2447", "desc": "Usermap_script remote command execution", "severity": "Critical"},
    "ISC BIND 9.4.2": {"cve": "Multiple", "desc": "Outdated DNS server, known DoS/cache poisoning issues", "severity": "Medium"},
    "UnrealIRCd": {"cve": "CVE-2010-2075", "desc": "Backdoor command execution", "severity": "Critical"},
}

def analyze(port, service_line):
    for signature, info in VULN_DB.items():
        if signature.split()[0].lower() in service_line.lower() and signature.split()[-1] in service_line:
            return {"port": port, "service": service_line, **info}
    return None
