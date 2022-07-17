import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

os.system("cls")
ip = input("Enter IP address: ")
url = f"https://ipapi.co/{ip}/json"
lookup = requests.get(url)

print(lookup.text)
