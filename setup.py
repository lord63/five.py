#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import five


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


setup(
    name='five',
    version=five.__version__,
    description='Gives you five. A library to overcomplicate `5`',
    long_description=long_description,
    url='http://github.com/lord63/five.py',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='five fun',
    packages=['five'],
    include_package_data=True
)
