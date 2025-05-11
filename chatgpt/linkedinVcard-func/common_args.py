import argparse
import os

def add_common_args(parser):
    parser.add_argument(
        "--vcardDir",
        required=True,
        help="Path to the directory where .vcf files are stored or will be written."
    )
    parser.add_argument(
        "--exportedZipFile",
        required=False,
        help="Path to the LinkedIn Basic_LinkedInDataExport_DATE.zip file."
    )
    parser.add_argument(
        "--linCsv",
        choices=["Connections.csv", "Invitations.csv", "Messages.csv"],w
        required=False,
        help="Specify the LinkedIn CSV file to process from the export."
    )
    return parser

def validate_common_args(args):
    if args.exportedZipFile and not os.path.isfile(args.exportedZipFile):
        raise FileNotFoundError(f"Zip file not found: {args.exportedZipFile}")

    if not os.path.isdir(args.vcardDir):
        os.makedirs(args.vcardDir, exist_ok=True)

    return True

"""
from common_args import add_common_args, validate_common_args
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process LinkedIn data.")
    add_common_args(parser)
    args = parser.parse_args()
    validate_common_args(args)

    print("vCard directory:", args.vcardDir)
    if args.exportedZipFile:
        print("Using export zip:", args.exportedZipFile)
    if args.linCsv:
        print("Processing CSV:", args.linCsv)

if __name__ == "__main__":
    main()

"""
