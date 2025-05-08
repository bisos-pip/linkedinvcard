
import vobject

def create_vcard(name, email, uid, note=None):
    vcard = vobject.vCard()
    vcard.add('fn').value = name
    vcard.add('n').value = vobject.vcard.Name(family=name.split()[-1], given=name.split()[0])
    vcard.add('email').value = email
    vcard.add('uid').value = uid
    if note:
        vcard.add('note').value = note
    return vcard.serialize()


import csv

def parse_invitations_csv(csv_path):
    invitations = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            invitations.append({
                "from": row["From"].strip(),
                "to": row["To"].strip(),
                "message": row.get("Message", "").strip(),
                "sent_at": row.get("Sent At", "").strip(),
            })
    return invitations



import os
import vobject

def augment_vcards_with_invitations(vcard_dir, invitations, your_name):
    for inv in invitations:
        if inv["from"] == your_name:
            inviter = "You"
            invitee = inv["to"]
        else:
            inviter = inv["from"]
            invitee = "You"

        linkedin_id = infer_linkedin_id(invitee if inviter == "You" else inviter)
        vcard_path = os.path.join(vcard_dir, linkedin_id + ".vcf")

        if os.path.exists(vcard_path):
            with open(vcard_path, "r", encoding="utf-8") as f:
                vcard = vobject.readOne(f)

            # Compose new note
            note_text = f"Invitation: From: {inv['from']} | To: {inv['to']}\nMessage: {inv['message']}\nDate: {inv['sent_at']}"
            vcard.add('note').value = note_text

            with open(vcard_path, "w", encoding="utf-8") as f:
                f.write(vcard.serialize())
