#!/usr/bin/env python
import re
from distutils.core import setup
from pathlib import Path

from setuptools import find_packages

ROOT = Path(__file__).parent
content = (ROOT / 'src/basicdate.py').read_text('utf-8')
readme = (ROOT / 'README.md').read_text('utf-8')

_references = {
    k: re.search(f'^{k.upper()}\s+=\s+"(.*)"\s*', content, re.MULTILINE).group(1)
    for k in [
        'version', 'name', 'author', 'author_email', 'description', 'license', 'url'
    ]
}

setup(
    **_references,
    keywords=['date', 'util'],
    entry_points={
    },
    package_dir={'': 'src'},
    py_modules=['basicdate', ],
    zip_safe=False,
    install_requires=['dateparser'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
    ]
)
