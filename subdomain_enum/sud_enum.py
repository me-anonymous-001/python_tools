import requests
import threading

domain = input("Enter the domain name: ")

with open("./subdomains.txt", "r") as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code:
            with lock:
                discovered_subdomains.append(url)
                print(f"Discovered: {url}")
    except requests.RequestException as e:
        print(f"Failed: {url} -> {e}")

threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open("./discovered_subdomains.txt", "w") as output_file:
    for subdomain in discovered_subdomains:
        output_file.write(subdomain + "\n")

print(" Subdomain enumeration completed. Discovered subdomains saved to discovered_subdomains.txt.")