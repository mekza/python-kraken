# coding=utf-8
import os
import re

from setuptools import find_packages
from setuptools import setup

import kraken 

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name = "python-kraken",
    version = kraken.__version__,
    description = kraken.__descr__,
    long_description = long_description,
    author = kraken.__author__,
    author_email = kraken.__author_mail__,
    license = "MIT License",
    url = kraken.__url__,
    keywords = kraken.__keywords__,
    classifiers = kraken.__classifiers__,
    packages = find_packages(),
    include_package_data = True,
    install_requires=['requests>=2.7.0'],
    zip_safe = False
)