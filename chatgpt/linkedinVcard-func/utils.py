import csv
from collections import defaultdict
from urllib.parse import urlparse

def build_name_to_id_map(connections_csv_path):
    name_to_id = defaultdict(list)
    with open(connections_csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            full_name = f"{row['First Name'].strip()} {row['Last Name'].strip()}"
            url = row["URL"].strip()
            if url:
                linkedin_id = url.rstrip('/').split('/')[-1]
                name_to_id[full_name].append(linkedin_id)
    return name_to_id


def infer_linkedin_id(name, name_to_id_map):
    ids = name_to_id_map.get(name, [])
    if not ids:
        print(f"[WARN] No LinkedIn ID found for: {name}")
        return None
    elif len(ids) > 1:
        print(f"[WARN] Multiple IDs found for: {name}, using first: {ids[0]}")
    return ids[0]

"""
 Usage Example

# Load name-to-id map once
name_to_id_map = build_name_to_id_map("Connections.csv")

# Then use like:
lid = infer_linkedin_id("Alice Smith", name_to_id_map)
"""
