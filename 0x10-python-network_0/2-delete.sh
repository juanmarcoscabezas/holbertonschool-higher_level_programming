#!/bin/bash

if [ $# -gt 0 ]; then
	curl -s -X DELETE "$1"
fi
