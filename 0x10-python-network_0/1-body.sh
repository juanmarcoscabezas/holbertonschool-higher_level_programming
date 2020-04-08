#!/bin/bash

if [ $# -gt 0 ]; then
	curl -L "$1"
fi
