#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" -L | grep "Allow" | awk -F: '{print $2}'
