from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='d1_generic',
    version='0.0.0',
    description='A Python D1 Generic client',
    license="Apache License, Version 2.0",
    long_description=long_description,
    packages=['d1_generic'],
)
