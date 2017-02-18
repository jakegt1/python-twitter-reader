#!/usr/bin/python3
from setuptools import setup

setup(
    name='twitter_reader',
    version='1.0',
    description='Small webapp for reading tweets on twitter.',
    author='Jake Torrance',
    author_email='jaket1234@hotmail.com',
    packages=['twitter_reader'],
    include_package_data=True,
    zip_safe=False,
    package_dir={'twitter_reader': 'src/twitter_reader'}
)
