#!/usr/bin/python3
"""Script that takes URL and a email, sends POST reques tto the URL"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)
