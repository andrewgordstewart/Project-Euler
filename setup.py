try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='project_euler_utilities',
	description='Project Euler tools',
	author='Andrew Stewart',
	url='Nonexistant.',
	download_url='Somewhere',
	author_email='kaptain.kayak@gmail.com',
	version='0.1',
	install_requires=['nose'],
    packages=['project_euler',
    			'project_euler.prime_tools',
				'project_euler.math_functions',
				'project_euler.string_tools']
)
