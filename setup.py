#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='npc2batman',
      version='1.0',
      description='Convert NPC NMR pipeline output data to meet BATMAN input',
      author='Noureddin Sadawi',
      author_email='n.sadawi@imperial.ac.uk',
      url='',
      scripts=["src/npc2batman.py"],
      install_requires=["pandas"],
      packages=find_packages(),
      )
