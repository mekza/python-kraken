# coding=utf-8
import os
import re

from setuptools import find_packages
from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = "python-kraken",
    version = "0.0.2",
    description = "Kraken API wrapper",
    long_description = long_description,
    author = "Martin-Zack Mekkaoui",
    author_email = "martin@mekkaoui.fr",
    license = "MIT License",
    url = "https://github.com/mekza/python-kraken/",
    keywords = 'Kraken python image optimizer',
    classifiers = [],
    packages = find_packages(),
    include_package_data = True,
    install_requires=['requests>=2.0.0'],
    zip_safe = False
)