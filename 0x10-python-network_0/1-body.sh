#!/bin/bash

if [ $# -gt 0 ]; then
	curl -sL "$1"
fi
