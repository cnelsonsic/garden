#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='Garden',
      version='0.1',
      description='Imagine if there was a category of games like "roguelike", but for garden/menagerie games. This is it.',
      author='Charles Nelson',
      author_email='cnelsonsic@gmail.com',
      url='https://github.com/cnelsonsic/garden',

      packages=find_packages(),

      install_requires = open('requirements.txt').read(),

      entry_points = {
          'console_scripts': [
              'garden = garden.garden:main',
              ],
          },
     )

