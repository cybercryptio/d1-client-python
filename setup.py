from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='d1-client-python',
    version='0.0.0',
    description='A Python D1 client',
    license="Apache License, Version 2.0",
    long_description=long_description,
    url="https://github.com/cybercryptio/d1-client-python",
    packages=['d1-client-python'],
    scripts=[
        'scripts/copy-client.sh',
    ]
)
