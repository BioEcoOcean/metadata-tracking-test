import os
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def generate_sitemap(json_folder, repo_url, output_file):
    """
    Generates a sitemap XML file for all JSON files in a folder.
    Args:
        json_folder (str): Path to the folder containing JSON files.
        repo_url (str): Base URL of the GitHub repo (e.g., https://github.com/username/repo).
        output_file (str): Path to save the sitemap.xml.
    """
    # Base URL for JSON files on GitHub
    repo_url = "https://github.com/BioEcoOcean/metadata-repo"
    json_folder = "jsonFiles"
    base_url = f"{repo_url}/blob/main/{json_folder}"
    
    # Create the root element of the sitemap
    urlset = Element("urlset", xmlns="https://www.sitemaps.org/schemas/sitemap/0.9")

    # Get a list of all JSON files in the directory
    for file_name in os.listdir(json_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(json_folder, file_name)
            
            # Extract changefreq from content[12] for each JSON file
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    changefreq = data.get("changefreq", "none")  # Default to "none" if not specified
                except json.JSONDecodeError:
                    print(f"Error reading {file_name}, skipping.")
                    continue

            # Create a URL entry in the sitemap
            url = SubElement(urlset, "url")
            loc = SubElement(url, "loc")
            loc.text = f"{base_url}/{file_name}"

            lastmod = SubElement(url, "lastmod")
            lastmod.text = datetime.date.today().isoformat()  # Current date as last modified date

            freq = SubElement(url, "changefreq")
            freq.text = changefreq

    # Write the XML to a file
    tree = ElementTree(urlset)
    with open(output_file, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print(f"Sitemap generated: {output_file}")

# Paths and URLs
JSON_FOLDER = "jsonFiles"  # Folder where JSON files are stored
REPO_URL = "https://github.com/BioEcoOcean/metadata-tracking-dev"  # Replace with your repo URL
OUTPUT_FILE = "sitemap.xml"

# Generate the sitemap
os.makedirs(JSON_FOLDER, exist_ok=True)  # Ensure the folder exists
generate_sitemap(JSON_FOLDER, REPO_URL, OUTPUT_FILE)
