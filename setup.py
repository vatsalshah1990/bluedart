#!/usr/bin/env python
from setuptools import setup
import bluedart

LONG_DESCRIPTION = open('README.md').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
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
      maintainer='Python Bluedart Developers',
      url='https://github.com/hornedbull/bluedart.git',
      download_url='http://pypi.python.org/pypi/bluedart/',
      packages=['bluedart'],
      package_dir={'bluedart': 'bluedart'},
      package_data={'bluedart': ['wsdl/*.wsdl', 'wsdl/test_server_wsdl/*.wsdl']},
      platforms=['Platform Independent'],
      license='BSD',
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      requires=['suds'],
      install_requires=['suds-jurko'],
      )
