#!/bin/bash

if [ $# -gt 0 ]; then
	curl -X PUT -H "Origin:HolbertonSchool" "$1"
fi
