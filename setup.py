#!/usr/bin/env python
from setuptools import setup

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setup(
    name='xontrib-up',
    version='1.0.0',
    license='MIT',
    author='mattmc3',
    author_email='ohmyxonsh@gmail.com',
    description="Go up any number of directories.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/oh-my-xonsh/xontrib-up',
    project_urls={
        "Documentation": "https://github.com/oh-my-xonsh/xontrib-up/blob/main/README.md",
        "Code": "https://github.com/oh-my-xonsh/xontrib-up",
        "Issue tracker": "https://github.com/oh-my-xonsh/xontrib-up/issues",
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Unix Shell",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
        "License :: OSI Approved :: MIT License"
    ]
)
