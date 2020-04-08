#!/bin/bash

if [ $# -gt 1 ]; then
	curl -s -H "Content-Type: application/json" -X POST "$1" -T "$2"
fi
