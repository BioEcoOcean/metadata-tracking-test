import json
import os
from datetime import datetime

# Define constants
REPO_ORG = "BioEcoOcean"
REPO_NAME = "metadata-tracking-dev"
BRANCH = "refs/heads/main"  # Update branch to include 'refs/heads'
JSON_FOLDER = "jsonFiles"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{REPO_ORG}/{REPO_NAME}/{BRANCH}/{JSON_FOLDER}"

def generate_sitemap():
    # Load all sitemap entries
    sitemap_entries = []
    for file_name in os.listdir("sitemap_data"):
        if file_name.endswith("_sitemap.json"):
            with open(f"sitemap_data/{file_name}", "r", encoding="utf-8") as f:
                entry = json.load(f)
                sitemap_entries.append(entry)

    # Generate sitemap XML
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for entry in sitemap_entries:
        sitemap += "  <url>\n"
        sitemap += f"    <loc>{entry['url']}</loc>\n"
        sitemap += f"    <lastmod>{entry['lastmod']}</lastmod>\n"
        sitemap += f"    <changefreq>{entry['changefreq']}</changefreq>\n"
        sitemap += "  </url>\n"
    sitemap += "</urlset>"

    # Save sitemap
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

    print("Sitemap generated successfully.")

if __name__ == "__main__":
    generate_sitemap()
