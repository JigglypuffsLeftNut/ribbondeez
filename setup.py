#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

from src.cli import _fversion, name, author, desc

setup(
    name=name,
    version=_fversion(),
    description=desc,
    author=author,
    url=f"https://github.com/{author}/{name}",
    license="",
    classifiers=[
    ],
    keywords=[
        name,
    ],
    packages=[
        name
    ],
    entry_points={
        "console_scripts": [
            f"{name}=src.cli:main"
        ]
    }
)
