#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "ape-base",  # Needed for Base networks integration
        "ape-optimism",  # Needed for Optimism integration
        "ape-polygon",  # Needed for Polygon integration
        "ape-infura",  # Needed for live network tests
        "ape-solidity",  # Needed for contract verification tests
        "pytest>=6.0",  # Core testing package
        "pytest-xdist",  # Multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
        "pytest-mock",  # Test mocker
    ],
    "lint": [
        "black>=24.3.0,<25",  # Auto-formatter and linter
        "mypy>=1.9.0,<2",  # Static type analyzer
        "types-setuptools",  # Needed for mypy type shed
        "types-requests",  # Needed for mypy type shed
        "flake8>=7.0.0,<8",  # Style linter
        "flake8-breakpoint>=1.1.0,<2",  # Detect breakpoints left in code
        "flake8-print>=5.0.0,<6",  # Detect print statements left in code
        "isort>=5.10.1,<6",  # Import sorting linter
        "mdformat>=0.7.17",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
        "mdformat-pyproject>=0.0.1",  # Allows configuring in pyproject.toml
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-blockscout",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ape-blockscout: Blockscout Explorer Plugin""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/ape-blockscout",
    include_package_data=True,
    install_requires=[
        "eth-ape>=0.7.0,<0.8",
        "requests",  # Use same version as eth-ape
    ],
    python_requires=">=3.8,<4",
    extras_require=extras_require,
    py_modules=["ape_blockscout"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_blockscout": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
