#!/bin/bash

if [ $# -gt 0 ]; then
	curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
fi
