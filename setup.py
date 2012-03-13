#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name= 'html2list',
      version='0.1.5',
      description='A library for converting html markup from an email or webpage into a list',
      long_description='',
      author='Ali Anari',
      author_email='ali@alianari.com',
      license='BSD',
      zip_safe=True,
      classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='https://github.com/aanari/html2list',
      keywords='python html email txt sms markup extraction',
      packages=find_packages()
    )
