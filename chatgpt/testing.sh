#!/usr/bin/env sh

generate_vcards --connectionsCsv Connections.csv --vcardDir vcards/
augment_vcards_invitations --vcardsDir vcards/ --invitationsCsv Invitations.csv
augment_vcards_messages --vcardsDir vcards/ --messagesCsv Messages.csv
