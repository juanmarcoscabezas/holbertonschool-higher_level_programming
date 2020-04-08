#!/bin/bash

if [ $# -gt 0 ]; then
	curl -si --stderr - "$1" | grep "Allow: " | cut -b 8-
fi
