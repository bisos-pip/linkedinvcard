#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='linkedin_vcard_tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'vobject',
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'generate_vcards = linkedin_vcard_tools.vcard_generator:main',
            'augment_vcards_invitations = linkedin_vcard_tools.vcard_augmenter:augment_with_invitations',
            'augment_vcards_messages = linkedin_vcard_tools.vcard_augmenter:augment_with_messages',
            'augment_vcards_remote = linkedin_vcard_tools.linkedin_scraper:augment_vcards_with_linkedin_data',
            'augment_vcards_external = linkedin_vcard_tools.external_data:augment_vcards_with_external_data',
        ],
    },
)
