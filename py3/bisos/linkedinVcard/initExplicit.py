"""
bisos.linkedin

This package provides tools for extracting, enriching, and converting LinkedIn
first-level connection data (from the LinkedIn Data Export) into vCard format.
It supports augmentation using local files such as Connections.csv,
Invitations.csv, and Messages.csv.
"""

from .connections import LinkedInConnections
from .invitations import LinkedInInvitations
from .messages import LinkedInMessages
from .augmentor import VCardAugmentor
from .utils import VCardUtils
