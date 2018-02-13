#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import open
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup
import re
import os
import sys

# get version
with open('loki/__init__.py', 'r', 'utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# use requirements.txt as deps list
with open('requirements.txt', 'r', 'utf-8') as f:
    required = f.read().splitlines()

# get readme
with open('docs/index.md', 'r', 'utf-8') as f:
    readme = f.read()

test_deps = ["green>=2.5.0", "coverage"]

setup(name='loki',
      packages=["loki"],
      version=version,
      keywords=['nlp', 'information extraction'],
      description="A simple language for information extraction based on Odin.",
      long_description=readme,
      url='http://github.com/myedibleenso/loki',
      download_url="https://github.com/myedibleenso/loki/archive/v{}.zip".format(version),
      author='myedibleenso',
      author_email='gushahnpowell@gmail.com',
      license='MIT',
      install_requires=required,
      classifiers=(
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
      ),
      tests_require=test_deps,
      extras_require={
        'test': test_deps
      },
      include_package_data=True,
      zip_safe=False)
