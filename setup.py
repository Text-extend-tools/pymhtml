from setuptools import setup, Extension
#from distutils.core import setup, Extension

setup(name='pymhtml',
	description='MHTML tools',
	author='Chema Gonzalez',
	author_email='chema@cal.berkeley.edu',
	url="http://github.com/chemag/libmhtml.py",
	version='0.0.1',
	#py_modules=['magic'],
	long_description="""This module provides an MHTML creator and parser.""",
	keywords="mhtml mht",
	license="BSD",
	install_requires = [
		'magic',
		'urlgrabber',
	],
	scripts = ['pymhtml']
	)

