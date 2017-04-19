#!/usr/bin/env python
"""Setup script of python module.

To install:
under windows, you must install the req_win_conda.tex
conda create -n py35 python=3.5 conda --file req_win_conda.txt
pip install .     => installs the module
pip install -e .  => the modules auto-updates when code inside is changed
                     (for developers)

alternatively
pip install -r requirements.txt
python setup.py install # for simple users
python setup.py develop # for developers
"""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('HISTORY.rst') as history_file:
    licence = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

setup(
  name='wepy',
  version='0.1',
  description='WePy package',
  url='https://github.com/Jul13/wepy.git',
  author='Julien Reynier',
  author_email='julien.reynier@gmail.com',
  license=licence,
  packages=['wepy'],
  package_dir={'wepy':
               'wepy'},
  install_requires=requirements,
  zip_safe=False,
  classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache 2.0',
      'Natural Language :: English',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
  ],
  test_suite='tests',
  tests_require=requirements
)
