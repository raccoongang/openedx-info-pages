#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os
import re

from setuptools import setup, find_packages


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('edx_info_pages', '__init__.py')

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;

    that is, it is not blank, a comment, a URL, or an included file.
    """
    return not (line == '' or line.startswith(('-r', '#', '-e', 'git+', '-c')))


setup(
    name='edx-info-pages',
    version=VERSION,
    install_requires=load_requirements("requirements/base.txt"),
    description="""Open-edx plugin with custom info pages""",
    long_description=README,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='edx info pages',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8.10',
    ],
    entry_points={
        "lms.djangoapp": [
            "edx_info_pages = edx_info_pages.apps:EdxInfoPagesConfig",
        ]
    }
)
