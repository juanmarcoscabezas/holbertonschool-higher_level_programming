#!/bin/bash

if [ $# -gt 0 ]; then
	curl -si --stderr - "$1" | grep "HTTP/1.0" | cut -b 10-12
fi
