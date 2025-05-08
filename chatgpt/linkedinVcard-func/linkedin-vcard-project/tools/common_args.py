import os

def add_common_args(parser):
    parser.add_argument(
        "--vcardDir",
        required=True,
        help="Directory where vCard files are stored or written."
    )
    parser.add_argument(
        "--exportedZipFile",
        required=False,
        help="Path to LinkedIn Basic_LinkedInDataExport_DATE.zip"
    )
    parser.add_argument(
        "--linCsv",
        choices=["Connections.csv", "Invitations.csv", "Messages.csv"],
        required=False,
        help="LinkedIn CSV file to process"
    )
    return parser

def validate_common_args(args):
    if args.exportedZipFile and not os.path.isfile(args.exportedZipFile):
        raise FileNotFoundError(f"Zip file not found: {args.exportedZipFile}")
    if not os.path.isdir(args.vcardDir):
        os.makedirs(args.vcardDir)
    return True