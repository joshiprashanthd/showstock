from setuptools import setup

from showstock import __appname__, __version__, __author__

setup(
    name=__appname__,
    version=__version__,
    author=__author__,
    packages=["showstock"],
    requires=["requests", "typer", "rich"],
    entry_points={"console_scripts": ["showstock = showstock.main:main"]},
)
