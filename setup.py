#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
briGit - Very simple git wrapper module
"""

from setuptools import find_packages, setup

VERSION = '1.2'


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
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-flake8', 'pytest-isort'],
    test_suite='brigit.test',
    use_2to3=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"])

setup(**options)
