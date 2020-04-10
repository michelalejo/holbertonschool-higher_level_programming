#!/bin/bash
# Script that displays the size of the body of the response.

curl -sI "$1" -X GET | grep "Content-Length" | cut -d ' ' -f2
