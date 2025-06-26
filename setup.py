# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : Tan_928
@Time    : 2025-06-10 05:04
@desc    : Setup configuration for md2xmind package
"""

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import setup, find_packages

setup(
    name='md2xmind',
    version='2.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'md2xmind = md2xmind.cli:main',  # 确保这里正确指向 cli.py 中的 main 函数
        ],
    },
    install_requires=[
        'xmind>=1.2.0',
    ],
    python_requires='>=3.6',
)