import requests

target = "http://demo.testfire.net"
# Hum in secret paths ko check karenge
folders = ["admin", "login", "api", "bank", "images", "js", "server-status"]

print(f"Searching for secret doors on {target}...")

for folder in folders:
    url = f"{target}/{folder}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"[+] FOUND: {url} (Ye darwaza khula hai!)")
    else:
        print(f"[-] Locked: {folder}")
