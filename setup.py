try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A single player zendo like game',
	'author': 'Matt Weems',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['zendo'],
	'scripts': [],
	'name': 'zendo'
}

setup(**config)
