# A minimal setup.py file to make a Python project installable.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]


setuptools.setup(
    name             = "gftt",
    version          = "0.0.1",
    author           = "The GFTT team",
    author_email     = "whyjz@berkeley.edu",
    description      = "Python module for testing glacier feature-tracking performance.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages         = setuptools.find_packages(),
    classifiers       = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires  = '>= 3.7',
    install_requires = requirements,
)