#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
briGit - Very simple git wrapper module
"""

from setuptools import setup, find_packages

VERSION = '1.0'


options = dict(
    name="brigit",
    version=VERSION,
    description="Very simple git wrapper module",
    long_description=__doc__,
    author="Florian Mounier - Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    install_requires=['log_colorizer'],
    provides=['brigit'],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"])

setup(**options)
