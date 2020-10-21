#!/usr/bin/env python3

# print("F", repr(__file__))
# print("P", repr(__package__))
# print("N", repr(__name__))

# __package__ = "mypackage.pyz"
# print("P2", repr(__package__))

from . import util
# from . import external.dateutil.Parser as dateutil_parser
from .external.dateutil import Parser as dateutil_parser

def main():
    print("hello from main.py")
    print(util.os_isfile("file"))
    print(dateutil_parser.is_magic_string("not magic"))

if __name__ == "__main__":
    main()
