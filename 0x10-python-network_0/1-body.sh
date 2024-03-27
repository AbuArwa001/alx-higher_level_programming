#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
status=$(curl -sI "$1" | grep "HTTP" | awk '{print $2}') && [ $status -eq 200 ] && curl $1
