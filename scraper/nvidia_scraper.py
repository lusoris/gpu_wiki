import json
import requests
from bs4 import BeautifulSoup
import os

def scrape_nvidia_gpus():
    url = "https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    gpu_list = []
    table = soup.find("table", {"class": "wikitable"})
    if not table:
        print("Nvidia GPU table not found!")
        return []

    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        gpu = {
            "name": cols[0].text.strip(),
            "codename": cols[1].text.strip(),
            "release_date": cols[2].text.strip()
        }
        gpu_list.append(gpu)

    return gpu_list

def save_nvidia_gpus(gpu_list):
    os.makedirs("data", exist_ok=True)
    with open("data/nvidia_gpus.json", "w") as f:
        json.dump(gpu_list, f, indent=2)

if __name__ == "__main__":
    gpus = scrape_nvidia_gpus()
    save_nvidia_gpus(gpus)
    print(f"Saved {len(gpus)} Nvidia GPUs.")
