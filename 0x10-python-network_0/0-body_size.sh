#!/bin/bash

if [ $# -gt 0 ]; then
	curl -si --stderr - "$1" | grep "Content-Length" | cut -d " " -f 2
fi
