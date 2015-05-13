#!/usr/bin/env python
# -*- coding: UTF-8 -*-

try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name = "CeleryTasks",
    version = '1.0',
    packages = find_packages(),
    namespace_packages = ['celerytasks'],
    requires = [],
    author = "Sergii Tretiak based on Dmitry Bogush",
    author_email = "tretyak@gmail.com",
    description = "A framework for wrapping celery tasks",
    long_description = open('README').read(),
    license = "LICENSE",
    keywords = "celery tasks join object",
    url = "https://github.com/xmig/celerytasks",
    include_package_data = True,
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)

