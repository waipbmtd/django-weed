#!/usr/bin/python

import os
from setuptools import setup, find_packages

from djweed.version import __version__


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


META_DATA = {
    'name': 'django-weed2',
    'version': __version__,
    'description': "Weed-FS integration into Django as a storage",
    'long_description': read('README.md'),
    'license': 'MIT',

    'author': "Devin",
    'author_email': "waipbmtd@gmail.com",

    'url': "https://github.com/waipbmtd/django-weed",

    'packages': find_packages(),

    'install_requires': ('django', 'pyseaweed>=0.3.3', 'six'),
}

if __name__ == "__main__":
    setup(**META_DATA)

