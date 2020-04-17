#!/usr/bin/python3
"""Script that takes in a URL, sends arequest to the URL, displays the value"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
