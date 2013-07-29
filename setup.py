#!/usr/bin/env python

from distutils.core import setup

setup(
	name='lightplay',
	version='1.0dev',
	packages=['lightplay',],
	license='BSD or something',
	long_description=open('README.md').read(),
	author = 'Brandon Thomas',
	author_email = 'bt@brand.io',
	requires = ['pygame(>=1.9.0)'],
)

