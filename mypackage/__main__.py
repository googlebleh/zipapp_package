#!/usr/bin/env python3

from . import util
# from . import external.dateutil.Parser as dateutil_parser
from .external.dateutil import Parser as dateutil_parser

def main():
    print("hello from main.py")
    print(util.os_isfile("file"))
    print(dateutil_parser.is_magic_string("not magic"))

if __name__ == "__main__":
    main()
