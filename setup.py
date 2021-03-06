import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='library-name',
    long_description=README,
    version='0.0.1',
    install_requires=[],
    packages=["example"],
    author='Leon Patmore',
    description=''
)
