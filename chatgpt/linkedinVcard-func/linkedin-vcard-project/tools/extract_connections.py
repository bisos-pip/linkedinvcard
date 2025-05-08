import csv
import os
import argparse
import vobject
from common_args import add_common_args, validate_common_args

def extract_connections(csv_path, output_dir):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row["URL"]
            linkedin_id = url.rstrip('/').split('/')[-1]
            fn = row["First Name"]
            ln = row["Last Name"]
            org = row["Company"]
            title = row["Position"]
            connected_on = row["Connected On"]

            card = vobject.vCard()
            card.add('fn').value = f"{fn} {ln}"
            card.add('n').value = vobject.vcard.Name(family=ln, given=fn)
            card.add('org').value = [org]
            card.add('title').value = title
            card.add('note').value = f"Connected On: {connected_on}"
            card.add('url').value = url

            with open(os.path.join(output_dir, f"{linkedin_id}.vcf"), 'w', encoding='utf-8') as f:
                f.write(card.serialize())

def main():
    parser = argparse.ArgumentParser(description="Extract connections to vCard files.")
    add_common_args(parser)
    args = parser.parse_args()
    validate_common_args(args)

    if args.linCsv != "Connections.csv":
        raise ValueError("This tool only works with Connections.csv")

    extract_connections(args.linCsv, args.vcardDir)

if __name__ == "__main__":
    main()