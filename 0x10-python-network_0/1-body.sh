#!/bin/bash
# Display only body of a 200 status code response #curl -sX GET $1 -L
cmd=$(($(curl -sI "$1" | grep HTTP | awk '{print $2}'))) && [ "$cmd" -eq "200" ] && curl -s "$1"
