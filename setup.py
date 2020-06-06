#!/usr/bin/env python3

from setuptools import setup
import gura

version = '0.1.0'
gura.__version__ = version

setup(name='gura',
      version=version,
      description='Gura live analyzes pitch from your microphone.',
      author='Viktor Blomqvist',
      #author_email='me@mail.com',
      packages=['gura'])
