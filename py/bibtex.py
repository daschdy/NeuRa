import os
import requests
from dotenv import load_dotenv

# Load environment variables
script_dir = os.path.dirname(os.path.realpath(__file__))
dotenv_path = os.path.join(script_dir, ".env")
load_dotenv(dotenv_path)

USER_ID = os.getenv("USER_ID")
API_KEY = os.getenv("API_KEY")
EXPORT_FORMAT = os.getenv("EXPORT_FORMAT", "bib")
PATH = os.path.abspath(os.path.join(script_dir, "..", "paper"))
COLLECTION_NAME = "NeuRa"
FILE_NAME = "thesis.bib"

# Step 1: Get all collections
collections_url = f"https://api.zotero.org/users/{USER_ID}/collections"
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(collections_url, headers=headers)

if response.status_code != 200:
    print("Error fetching collections:", response.status_code, response.text)
    exit(1)

collections = response.json()
collection_key = None

# Step 2: Find the key for COLLECTION_NAME
for collection in collections:
    if collection["data"]["name"] == COLLECTION_NAME:
        collection_key = collection["key"]
        break

if not collection_key:
    print(f"Collection '{COLLECTION_NAME}' not found.")
    exit(1)

# Helper function for fetching all paginated results
def fetch_all_items(url, headers):
    items = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Error fetching items:", response.status_code, response.text)
            break

        items.append(response.text)

        # Handle pagination
        if "Link" in response.headers:
            links = response.headers["Link"].split(",")
            next_link = None
            for link in links:
                if 'rel="next"' in link:
                    next_link = link[link.find("<")+1:link.find(">")]
                    break
            url = next_link
        else:
            url = None
    return "".join(items)

# Step 3: Export items from the collection (all, not just top-level)
export_url = f"https://api.zotero.org/users/{USER_ID}/collections/{collection_key}/items?format={EXPORT_FORMAT}"
bibtex = fetch_all_items(export_url, headers)

# Step 4: Save to file
target = os.path.join(PATH, FILE_NAME)
with open(target, "w", encoding="utf-8") as f:
    f.write(bibtex)

print(f"Export successful! File saved as {target}")
