#!/bin/bash

if [ $# -gt 0 ]; then
	curl -i --stderr - 0:5000/route_4 | grep "Allow: " | cut -b 8-
fi
