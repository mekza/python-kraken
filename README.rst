python-kraken |Build Status|
============================

Unofficial Kraken module for Python

Installation
------------

Method with pip: if you have pip installed, just type this in a terminal
(sudo is optional on some systems)

::

    pip install python-kraken

Method by hand: download the sources, either on PyPI or (if you want the
development version) on Github, unzip everything in one folder, open a
terminal and type

::

    python setup.py install

Usage
-----

.. code:: python

    >>> from kraken import Kraken
    >>> kr = Kraken('API_KEY', 'API_SECRET')
    >>> kr.url("http://my-awesome-website.com/image.jpg", wait=True)

.. |Build Status| image:: https://travis-ci.org/mekza/python-kraken.svg
   :target: https://travis-ci.org/mekza/python-kraken