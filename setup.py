#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

from moe_crawler import __version__


tests_require = [
    'mock',
    'pytest',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='moe-crawler',
    version=__version__,
    description='Web crawler to download your favorite images.',
    long_description='''
Web crawler to download your favorite images.
''',
    keywords='crawler',
    author='kxxoling',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/moe-crawler',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'requests',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'moe-crawler=moe_crawler.cli:main',
        ],
    },
)
