import csv
import os
import vobject

class LinkedInInvitations:
    """
    Processes Invitations.csv to annotate vcards with invitation direction and message.
    """

    def __init__(self, csv_path):
        """
        Initialize with the path to Invitations.csv.
        """
        self.csv_path = csv_path
        self.invitations = []

    def load(self):
        """
        Load invitation records from CSV into memory.
        """
        with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.invitations = list(reader)

    def augment_vcards(self, vcard_dir):
        """
        Add invitation direction and message to matching vCards.
        """
        if not self.invitations:
            self.load()

        for invitation in self.invitations:
            profile_url = invitation.get('To Profile URL') or invitation.get('From Profile URL')
            if not profile_url:
                continue
            uid = profile_url.rstrip('/').split('/')[-1]
            vcard_path = os.path.join(vcard_dir, uid + '.vcf')

            if not os.path.exists(vcard_path):
                continue

            with open(vcard_path, 'r', encoding='utf-8') as f:
                vcard = vobject.readOne(f.read())

            direction = "Sent" if invitation.get('To Profile URL') else "Received"
            message = invitation.get('Message', '').strip()

            note_value = f"Invitation {direction}"
            if message:
                note_value += f" — {message}"

            if 'note' in vcard.contents:
                vcard.note.value += f"\n{note_value}"
            else:
                vcard.add('note').value = note_value

            with open(vcard_path, 'w', encoding='utf-8') as f:
                f.write(vcard.serialize())
