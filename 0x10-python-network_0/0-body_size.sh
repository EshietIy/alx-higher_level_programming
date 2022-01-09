#!/bin/bash
# bash script that takes in url and makes http request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
