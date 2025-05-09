import csv
import os
import vobject
from collections import defaultdict

class LinkedInMessages:
    """
    Processes Messages.csv to annotate vCards with message history from first-level connections.
    """

    def __init__(self, csv_path):
        """
        Initialize with the path to Messages.csv.
        """
        self.csv_path = csv_path
        self.messages_by_uid = defaultdict(list)

    def load(self):
        """
        Load and group messages by LinkedIn user ID (from Profile URL).
        """
        with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                profile_url = row.get("Profile URL", "").strip()
                if not profile_url:
                    continue
                uid = profile_url.rstrip('/').split('/')[-1]
                sender = row.get("From", "").strip()
                content = row.get("Content", "").strip()
                date = row.get("Date", "").strip()
                message = f"{date} — {sender}: {content}"
                self.messages_by_uid[uid].append(message)

    def augment_vcards(self, vcard_dir):
        """
        Add messages as notes to corresponding vCards.
        """
        if not self.messages_by_uid:
            self.load()

        for uid, messages in self.messages_by_uid.items():
            vcard_path = os.path.join(vcard_dir, uid + '.vcf')
            if not os.path.exists(vcard_path):
                continue

            with open(vcard_path, 'r', encoding='utf-8') as f:
                vcard = vobject.readOne(f.read())

            note_value = "Messages:\n" + "\n".join(messages)

            if 'note' in vcard.contents:
                vcard.note.value += f"\n{note_value}"
            else:
                vcard.add('note').value = note_value

            with open(vcard_path, 'w', encoding='utf-8') as f:
                f.write(vcard.serialize())
