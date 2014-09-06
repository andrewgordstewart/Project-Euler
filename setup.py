try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='proj_eul',
	description='Project Euler tools',
	author='Andrew Stewart',
	url='Nonexistant.',
	download_url='Somewhere',
	author_email='kaptain.kayak@gmail.com',
	version='0.1',
	install_requires=['nose'],
    packages=['proj_eul',
    			'proj_eul.prime_tools',
				'proj_eul.math_tools',
				'proj_eul.string_tools']
)
