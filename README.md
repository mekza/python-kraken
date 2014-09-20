python-kraken
=============

Official Kraken module for Python

## Installation

Method with pip: if you have pip installed, just type this in a terminal (sudo is optional on some systems)

```
(sudo) pip install python-kraken
```

Method by hand: download the sources, either on PyPI or (if you want the development version) on Github, unzip everything in one folder, open a terminal and type

```
(sudo) python setup.py install
```


## Usage

```
>>> from kraken import Kraken
>>> Kraken.api_key = 'your-key'
>>> Kraken.api_secret = 'your-secret'
>>> Kraken.url("http://my-awesome-website.com/image.jpg", wait=True)
```

