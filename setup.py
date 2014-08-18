try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	# 'description': 'Project Euler utilities',
	'author': 'Andrew Stewart',
	'url': 'Nonexistant.',
	'download_url': 'Somewhere',
	'author_email': 'kaptain.kayak@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'modules': [],
	'packages': ['project_euler', 'project_euler.math_functions'],
	'scripts': [],
	'name': 'project_euler_utilities'
}

setup(**config)
