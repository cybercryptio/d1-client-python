from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='d1_client_python',
    description='A Python D1 client',
    license="Apache License, Version 2.0",
    long_description=long_description,
    url="https://github.com/cybercryptio/d1-client-python",
    packages=['d1_generic', 'd1_storage'],
    scripts=[
        'scripts/copy-client.sh',
    ]
)
