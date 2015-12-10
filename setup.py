#!/usr/bin/env python
from setuptools import setup


setup(
    name='apispec_restful',
    version='0.1.0-dev0',
    license='BSD',
    author='Andrew Pashkin',
    author_email='andrew.pashkin@gmx.co.uk',
    py_modules=['apispec_restful'],
    install_requires=['PyYAML>=3,<4'],
    include_package_data=True
)
