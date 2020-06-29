#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='intake-auth',
    version='0.0.1',
    description='Server side authentication',
    ulr='',
    maintainer='Tom Mertens',
    maintainer_email='',
    packages=find_packages(),
    entry_points={
        'intake.drivers': [
            'intake-server-auth = intake_server_auth.intake_server_auth:SecretAuth'
        ]
    },
    include_package_data=True,
    install_requires=['intake'],
    long_description='',
    zip_safe=False
)
