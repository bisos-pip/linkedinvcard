import argparse
import os

def merge_vcards(vcard_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for filename in os.listdir(vcard_dir):
            if filename.endswith('.vcf'):
                with open(os.path.join(vcard_dir, filename), 'r', encoding='utf-8') as f:
                    out.write(f.read() + '\n')

def main():
    parser = argparse.ArgumentParser(description="Merge vCards into one .vcf")
    parser.add_argument("--vcardDir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    merge_vcards(args.vcardDir, args.output)

if __name__ == "__main__":
    main()