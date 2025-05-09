import csv
import os
import vobject

class LinkedInConnections:
    """
    Handles parsing of Connections.csv and creation of base vCards for each connection.
    """

    def __init__(self, csv_path):
        """
        Initialize with the path to Connections.csv.
        """
        self.csv_path = csv_path
        self.connections = []

    def load(self):
        """
        Load connection records from CSV into memory.
        """
        with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.connections = list(reader)

    def create_vcards(self, output_dir):
        """
        Create and write vCard files for each connection.
        """
        if not self.connections:
            self.load()

        os.makedirs(output_dir, exist_ok=True)

        for entry in self.connections:
            vcard = vobject.vCard()
            vcard.add('fn').value = entry['First Name'] + ' ' + entry['Last Name']
            vcard.add('n').value = vobject.vcard.Name(family=entry['Last Name'], given=entry['First Name'])
            vcard.add('note').value = f"Connected On: {entry['Connected On']}"
            vcard.add('org').value = [entry.get('Company', '')]
            vcard.add('title').value = entry.get('Position', '')

            url = entry.get('URL', '')
            if url:
                vcard.add('url').value = url
                uid = url.rstrip('/').split('/')[-1]
            else:
                uid = entry['First Name'] + '_' + entry['Last Name']

            filename = os.path.join(output_dir, uid + '.vcf')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(vcard.serialize())
