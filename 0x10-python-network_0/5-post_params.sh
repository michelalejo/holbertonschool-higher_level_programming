#!/bin/bash
# Script that takes in a URL, sends a POST request.
curl "$1" -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
