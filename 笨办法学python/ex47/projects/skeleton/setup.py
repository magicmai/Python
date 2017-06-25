try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Magic Mai',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'maijing_wy@163.com',
	'version': '0.1',
	'install_requires': ['none'],
	'package': ['ex47'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)