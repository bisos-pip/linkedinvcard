import vobject
import os

class VCardAugmentor:
    """
    Adds additional data from LinkedIn Data Export files into existing vCards.
    """

    def __init__(self, connections_csv, invitations_csv, messages_csv):
        """
        Initialize with paths to Connections.csv, Invitations.csv, and Messages.csv.
        """
        self.connections_csv = connections_csv
        self.invitations_csv = invitations_csv
        self.messages_csv = messages_csv

    def augment_vcards(self, vcard_dir):
        """
        Augments vCards in the given directory using local CSV files.
        """
        # Process each CSV and augment vCards
        self.augment_connections(vcard_dir)
        self.augment_invitations(vcard_dir)
        self.augment_messages(vcard_dir)

    def augment_connections(self, vcard_dir):
        """
        Augment vCards with data from Connections.csv (e.g., position, company).
        """
        with open(self.connections_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                uid = row.get("LinkedIn ID")
                if not uid:
                    continue

                vcard_path = os.path.join(vcard_dir, f"{uid}.vcf")
                if not os.path.exists(vcard_path):
                    continue

                with open(vcard_path, 'r', encoding='utf-8') as vcard_file:
                    vcard = vobject.readOne(vcard_file.read())

                if "Company" in row:
                    vcard.org.value = row["Company"]
                if "Position" in row:
                    vcard.title.value = row["Position"]

                with open(vcard_path, 'w', encoding='utf-8') as vcard_file:
                    vcard_file.write(vcard.serialize())

    def augment_invitations(self, vcard_dir):
        """
        Augment vCards with invitation data from Invitations.csv (e.g., invite type, message).
        """
        with open(self.invitations_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                uid = row.get("LinkedIn ID")
                if not uid:
                    continue

                vcard_path = os.path.join(vcard_dir, f"{uid}.vcf")
                if not os.path.exists(vcard_path):
                    continue

                with open(vcard_path, 'r', encoding='utf-8') as vcard_file:
                    vcard = vobject.readOne(vcard_file.read())

                invite_type = row.get("Invitation Type")
                message = row.get("Invitation Message")

                if invite_type:
                    vcard.add('note').value = f"Invitation Type: {invite_type}"
                if message:
                    vcard.add('note').value += f"\nInvitation Message: {message}"

                with open(vcard_path, 'w', encoding='utf-8') as vcard_file:
                    vcard_file.write(vcard.serialize())

    def augment_messages(self, vcard_dir):
        """
        Augment vCards with message history data from Messages.csv.
        """
        with open(self.messages_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                uid = row.get("LinkedIn ID")
                if not uid:
                    continue

                vcard_path = os.path.join(vcard_dir, f"{uid}.vcf")
                if not os.path.exists(vcard_path):
                    continue

                with open(vcard_path, 'r', encoding='utf-8') as vcard_file:
                    vcard = vobject.readOne(vcard_file.read())

                message_content = row.get("Message Content")
                if message_content:
                    if 'note' in vcard.contents:
                        vcard.note.value += f"\nMessage: {message_content}"
                    else:
                        vcard.add('note').value = f"Message: {message_content}"

                with open(vcard_path, 'w', encoding='utf-8') as vcard_file:
                    vcard_file.write(vcard.serialize())
