#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
briGit - Very simple git wrapper module
"""

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
    install_requires=['log_colorizer'],
    classifiers=[
        "Development Status :: WIP",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"])

setup(**options)
