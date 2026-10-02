cd ~/vuln-scanner
cat > README.md << 'EOF'
# Network Vulnerability Scanner

A Python tool that scans a target IP for open ports and service versions using Nmap, cross-references them against a database of known CVEs, and generates an HTML vulnerability report.

## Tools
Python 3, python-nmap, Nmap

## How it works
1. `scanner.py` scans the target (1-1000 TCP ports, service version detection)
2. `analyzer.py` matches detected services against known-vulnerable signatures
3. `report.py` outputs findings as a color-coded HTML report

## Usage
