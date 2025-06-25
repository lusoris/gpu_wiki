import json

def generate_fancy_wiki(json_path, md_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    vendors = {}
    for gpu in data:
        vendor = gpu.get("vendor", "Unknown").title()
        if vendor not in vendors:
            vendors[vendor] = []
        vendors[vendor].append(gpu)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# GPU Architectures & Codecs\n\n")
        f.write("Welcome to the GPU data wiki!  \nBrowse architectures, vendors, devices, and supported video codecs.\n\n---\n\n")
        f.write("## Table of Contents\n\n")
        for vendor in vendors:
            f.write(f"- [{vendor}](#{vendor.lower()})\n")
        f.write("\n---\n\n")

        for vendor, gpus in vendors.items():
            f.write(f"## {vendor}\n\n")
            f.write("<details>\n")
            f.write(f"<summary><strong>All {vendor} GPUs</strong></summary>\n\n")
            f.write("| Device Name | Device ID | Architecture | Codename | iGPU? | Encode Codecs | Decode Codecs |\n")
            f.write("|-------------|-----------|--------------|----------|-------|---------------|---------------|\n")
            for gpu in gpus:
                name = gpu.get("device_name", "N/A")
                dev_id = gpu.get("device_id", "N/A")
                arch = gpu.get("architecture", "N/A")
                codename = gpu.get("codename", "N/A")
                igpu = "Yes" if gpu.get("is_igpu", False) else "No"
                encode = gpu.get("codecs", {}).get("encode", [])
                decode = gpu.get("codecs", {}).get("decode", [])
                if isinstance(encode, dict):
                    encode_str = ", ".join(f"{k}: {v}" for k,v in encode.items())
                    decode_str = ", ".join(f"{k}: {v}" for k,v in decode.items())
                else:
                    encode_str = ", ".join(encode) if encode else "None"
                    decode_str = ", ".join(decode) if decode else "None"

                f.write(f"| {name} | {dev_id} | {arch} | {codename} | {igpu} | {encode_str} | {decode_str} |\n")

            f.write("</details>\n\n---\n\n")

        # search box
        f.write("""# Search box

<input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Search for devices.." style="width: 100%; padding: 12px; margin-bottom: 10px; font-size: 16px;">

<script>
function searchTable() {
  var input, filter, tables, tr, td, i, j, txtValue;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  tables = document.querySelectorAll("table");
  tables.forEach(table => {
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
      let visible = false;
      let tds = tr[i].getElementsByTagName("td");
      for (j = 0; j < tds.length; j++) {
        td = tds[j];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            visible = true;
            break;
          }
        }
      }
      tr[i].style.display = visible ? "" : "none";
    }
  });
}
</script>
""")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python wiki_generator.py <input_json> <output_md>")
        exit(1)
    generate_fancy_wiki(sys.argv[1], sys.argv[2])
