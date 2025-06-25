import json
import requests

# NOTE: Replace URLs with your actual data sources
NVIDIA_JSON_URL = "https://raw.githubusercontent.com/user/repo/main/nvidia_gpus.json"
AMD_JSON_URL = "https://raw.githubusercontent.com/user/repo/main/amd_gpus.json"
INTEL_JSON_URL = "https://raw.githubusercontent.com/user/repo/main/intel_gpus.json"

def fetch_json(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def unify_gpu_data(*vendor_data_lists):
    seen = set()
    unified = []
    for vendor_list in vendor_data_lists:
        for gpu in vendor_list:
            # Create a deduplication key (vendor + device_id)
            key = (gpu.get("vendor","").lower(), gpu.get("device_id","").lower())
            if key in seen:
                continue
            seen.add(key)
            unified.append(gpu)
    return unified

def main():
    nvidia = fetch_json(NVIDIA_JSON_URL)
    amd = fetch_json(AMD_JSON_URL)
    intel = fetch_json(INTEL_JSON_URL)

    unified = unify_gpu_data(nvidia, amd, intel)

    with open("gpu_unified.json", "w", encoding="utf-8") as f:
        json.dump(unified, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
