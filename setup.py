#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="nix-google-fonts-gen",
    version=0.1,
    author="Samuel Laurén",
    description="Generate Nix package overlay from Google Fonts repository.",
    url="https://github.com/Soft/nix-google-fonts-gen",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["nix-google-fonts-gen=nix_google_fonts_gen.cli:main"]
    },
    install_requires=["protobuf", "dataclasses", "unidecode"],
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Fonts",
        "Topic :: System :: Archiving :: Packaging",
        "License :: OSI Approved :: Apache Software License"
    ],
)
