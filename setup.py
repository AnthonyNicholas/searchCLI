#!/usr/bin/env python
from distutils.core import setup
import setuptools

import os
from setuptools import setup


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_path = os.path.join(".", "requirements.txt")
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs


setup(
    name="ZenDeskSearch",
    version="0.1",
    description="technical test",
    author="various",
    author_email="russelljarvis@protonmail.com",
    url="https://github.com/russelljjarvis/searchCLI",
    packages=setuptools.find_packages(),
)
# os.system('sudo bash pip install -r requirements.txt')
# os.system('sudo bash install/user_install.sh')
# import nltk
# import nltk; nltk.download('punkt')
# import nltk; nltk.download('stopwords')
