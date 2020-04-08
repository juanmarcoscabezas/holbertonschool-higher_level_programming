#!/bin/bash

if [ $# -gt 0 ]; then
	curl "$1"
fi
