from vcard_generator import VCardGenerator

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate vCards from Connections.csv")
    parser.add_argument('--connectionsCsv', required=True, help="Path to Connections.csv file")
    parser.add_argument('--vcardDir', required=True, help="Directory to store generated vCards")
    args = parser.parse_args()

    generator = VCardGenerator(args.connectionsCsv, args.vcardDir)
    generator.generate_vcards()

if __name__ == "__main__":
    main()
