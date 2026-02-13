import requests

target = "http://demo.testfire.net/admin"
files = ["index.php", "login.jsp", "login.html", "config.php", "users.xml", "database.sql"]

print(f"Investigating the Admin Vault: {target}...")

for file in files:
    url = f"{target}/{file}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[!!!] SENSITIVE FILE FOUND: {url}")
        else:
            print(f"[-] Locked: {file}")
    except:
        print(f"[!] Error checking: {file}")
