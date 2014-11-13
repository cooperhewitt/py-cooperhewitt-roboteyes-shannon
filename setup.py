#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.roboteyes.shannon',
    namespace_packages=['cooperhewitt', 'cooperhewitt.roboteyes'],
    version='0.2',
    description='',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-shannon',
    requires=[],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-shannon/tarball/master',
    license='BSD')
