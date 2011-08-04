#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
briGit - Very simple git wrapper module
"""

import sys
from setuptools import setup, find_packages

# Use a time-based version number with ridiculous precision as pip in tox
# does not reinstall the same version.
import datetime
VERSION = "git-" + datetime.datetime.now().isoformat()


options = dict(
    name="brigit",
    version=VERSION,
    description="Very simple git wrapper module",
    long_description=__doc__,
    author="Florian Mounier - Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    packages=find_packages(),
    classifiers=[
        "Development Status :: WIP",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Libraries :: Python Modules"])

if sys.version_info >= (3,):
    options['use_2to3'] = True

setup(**options)
