#!/bin/bash

if [ $# -gt 0 ]; then
	curl -X DELETE "$1"
fi
