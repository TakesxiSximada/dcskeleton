#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )


def read_requirements(path):
    if os.path.exists(path):
        with open(path, 'rt') as fp:
            return [line.strip() for line in fp]
    return []


def read_readme(path):
    if os.path.exists(path):
        with open(path, 'rb') as fp:
            return fp.read().decode()
    return ''

src = 'src'
requirements_default = read_requirements('requirements.txt')
setup(
    name='dcskeleton',
    version='0.1',
    url='https://github.com/TakesxiSximada/dcskeleton',
    download_url='https://github.com/TakesxiSximada/dcskeleton',
    license='See http://www.python.org/3.4/license.html',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="0.1.0",
    long_description=(read_readme('README.rst') or read_readme('README.md') or '0.1.0'),
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=find_packages(src),
    package_dir={'': src},
    namespace_packages=[
        ],
    package_data={},
    include_package_data=True,
    install_requires=(read_requirements('requirements/install.txt') or requirements_default),
    test_require=(read_requirements('requirements/test.txt') or requirements_default),
    entry_points='''
    [console_scripts]
    '''
    )
