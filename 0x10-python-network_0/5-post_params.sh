#!/bin/bash

if [ $# -gt 0 ]; then
	curl -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" 0:5000 "$1"
fi
