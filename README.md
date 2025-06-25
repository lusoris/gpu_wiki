# GPU Architectures & Codecs Wiki Generator

This project scrapes and unifies GPU architecture data from NVIDIA, AMD, and Intel sources, then generates a fancy markdown wiki page listing GPUs and supported codecs.

## Files

- `scraper_parser.py`: Fetches JSON data from upstream sources, unifies and deduplicates it into `gpu_unified.json`.
- `wiki_generator.py`: Generates a markdown wiki file `GPU_WIKI.md` from `gpu_unified.json`.
- `.github/workflows/update_gpu_wiki.yml`: GitHub Action workflow to automate running scripts daily, committing and pushing changes, and updating the GitHub Wiki.

## Usage

1. Update URLs in `scraper_parser.py` to point to your upstream JSON sources.
2. Commit all files to your repo.
3. The GitHub Action runs daily at 02:00 UTC and on manual trigger.
4. The action updates `gpu_unified.json` and `GPU_WIKI.md`, commits changes, and pushes to main branch.
5. It also updates your GitHub Wiki with the new markdown page.

---

# Customization

- Modify the python scripts to match your data structure if needed.
- Customize the markdown template in `wiki_generator.py` for styling.

---

# Requirements

- Python 3.8+
- `requests` package for HTTP fetch

---

# License

Your choice.
