import requests
from datetime import datetime

def fetch_cld_api():
    url = "https://api.chongluadao.vn/v2/blacklist"

    response = requests.get(url)
    if response.status_code == 200:
        cld_output = response.json()
        return cld_output
    else:
        print("Failed to fetch from CLD api.")
        return []

def generate_blocklist(output_file):
    cld_output = fetch_cld_api()
    if not cld_output:
        return

    current_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"! Title: ChongLuaDao Blocklist\n")
        file.write(f"! Updated: {current_time}\n")
        file.write(f"! Expires: 1 day\n")
        file.write(f"! Homepage: https://chongluadao.vn\n")
        file.write(f"! Author: 7onez, Hung Nguyen\n")
        file.write(f"\n")
        for cld in cld_output:
            url = cld["url"].replace("http://", "").replace("https://", "").replace("/", "")
            file.write(f"||.{url}^\n")
    print(f"OK")

output_file = "chongluadao.txt"
generate_blocklist(output_file)
