#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages

__version__ = None
with open("qytPython/version.py") as f:
    exec(f.read())

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    reqs = f.read()

pkgs = [p for p in find_packages() if p.startswith('qytPython')]
print(pkgs)

setup(
    name='qytPython',
    version=__version__,
    url='https://github.com/q759729997/qytPython',
    description='qytPython: Python tools',
    long_description=readme,
    long_description_content_type='text/markdown',
    license=license,
    author='qiaoyongtian',
    python_requires='>=3.6',
    packages=pkgs,
    install_requires=reqs.strip().split('\n'),
)
