#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-copper",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_copper"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-copper=tap_copper:main
    """,
    packages=["tap_copper"],
    package_data = {
        "schemas": ["tap_copper/schemas/*.json"]
    },
    include_package_data=True,
)
