from datetime import datetime

def generate_report(findings, target, filename="report.html"):
    html = f"""
    <html><head><title>Vulnerability Report</title>
    <style>
    body {{ font-family: Arial; margin: 40px; }}
    h1 {{ color: #222; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
    .Critical {{ background: #ffcccc; }}
    .High {{ background: #ffe0b3; }}
    .Medium {{ background: #fff5cc; }}
    </style></head><body>
    <h1>Vulnerability Assessment Report</h1>
    <p><b>Target:</b> {target}<br><b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    <table>
    <tr><th>Severity</th><th>Port</th><th>Service</th><th>Issue</th><th>CVE</th></tr>
    """
    for f in findings:
        html += f"<tr class='{f['severity']}'><td>{f['severity']}</td><td>{f['port']}</td><td>{f['service']}</td><td>{f['desc']}</td><td>{f['cve']}</td></tr>"
    html += "</table></body></html>"

    with open(filename, "w") as f:
        f.write(html)
    print(f"Report saved to {filename}")
