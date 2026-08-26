import requests
import re
from datetime import datetime

def get_latest_cves():
    # CIRCL CVE API üzerinden en son 5 zafiyeti çekiyoruz (Hızlı ve anahtarsız API)
    url = "https://cve.circl.lu/api/last/5"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        cves = response.json()
        
        table_rows = []
        for cve in cves:
            cve_id = cve.get("id", "N/A")
            # CVSS Puanı ve Seviyesi
            cvss = cve.get("cvss", "N/A")
            severity = "🔴 High/Crit" if cvss != "N/A" and float(cvss) >= 7.0 else "🟡 Medium" if cvss != "N/A" and float(cvss) >= 4.0 else "🟢 Low"
            
            # Açıklamayı kısalt
            summary = cve.get("summary", "No summary provided.")
            summary = (summary[:75] + '...') if len(summary) > 75 else summary
            summary = summary.replace("|", "-").replace("\n", " ") # Markdown tablosunu bozmasın
            
            # Tarih
            published = cve.get("Published", "").split("T")[0]
            
            table_rows.append(f"| [{cve_id}](https://nvd.nist.gov/vuln/detail/{cve_id}) | {severity} ({cvss}) | {summary} | {published} |")
            
        return "\n".join(table_rows)
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return "| N/A | N/A | Veri çekilemedi | N/A |"

def update_readme():
    cve_data = get_latest_cves()
    
    table_header = "| CVE ID | Severity (CVSS) | Summary | Date |\n| :--- | :--- | :--- | :--- |\n"
    new_content = f"<!-- CVE-START -->\n{table_header}{cve_data}\n<!-- CVE-END -->"
    
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
        
    pattern = r"<!-- CVE-START -->.*?<!-- CVE-END -->"
    updated_readme = re.sub(pattern, new_content, readme, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    update_readme()
  
