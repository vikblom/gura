#!/usr/bin/env python3
from setuptools import setup, find_packages

version = '0.1.0'

setup(name='gura',
      version=version,
      description='Gura live analyzes pitch from your microphone.',
      author='Viktor Blomqvist',
      #author_email='me@mail.com',
      packages=find_packages(exclude=('tests', 'docs')))
