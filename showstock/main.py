from showstock import __appname__
from . import cli


def main():
    cli.app(prog_name=__appname__)
