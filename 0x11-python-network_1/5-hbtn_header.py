#!/usr/bin/python3
"""Script that takes URL and a email, sends POST reques tto the URL"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))