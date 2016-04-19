#!/usr/bin/env python
from setuptools import setup
import bluedart

LONG_DESCRIPTION = """
Python BlueDart SOAP API Module
===============================

:Author: Vatsal Shah
:Maintainer: Vatsal Shah
:License: BSD
:Status: Stable

What is it?
-----------

A light wrapper around Bluedart's Webservice Soap API. I don't do much of any
validation, but I'll help you sort through the pile of SOAP objects BlueDart
uses.

Installation
------------

The easiest way is via pip or easy_install::

    pip install bluedart

Quick Start
-----------

- Clone this repository.

- Edit the `example_profile.py` file in See `examples/ <examples/>`_ with your bluedart credentials
and run any of the provided examples.


Support
-------

Issues & Questions: https://github.com/hornedbull/bluedart/issues

Most problems are going to require investigation or a submitted
pull request.
To contribute a new feature or service, feel free to create a pull request.
We are always looking for new contributors to help maintain the project.


Todos
-----

- Increase service specific request validation
- Remove deprecated services (package movement service)

Legal
-----

Copyright (C) 2008-2016 Vatsal Shah

This software is licensed under the MIT License.
"""

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'bluedart soap suds wrapper rate location ship service'

setup(name='bluedart',
      version=bluedart.VERSION,
      description='Bluedart Web Services API wrapper.',
      long_description=LONG_DESCRIPTION,
      author='Vatsal Shah',
      author_email='shahvatsal90@gmail.com',
      maintainer='Vatsal Shah',
      url='https://github.com/hornedbull/bluedart.git',
      download_url='http://pypi.python.org/pypi/bluedart/',
      packages=['bluedart'],
      package_dir={'bluedart': 'bluedart'},
      platforms=['Platform Independent'],
      license='MIT',
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      requires=['suds'],
      install_requires=['suds-jurko'],
      )
