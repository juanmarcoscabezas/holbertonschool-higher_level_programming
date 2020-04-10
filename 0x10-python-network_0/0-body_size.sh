#!/bin/bash

curl -si --stderr - "$1" | grep "Content-Length" | cut -d " " -f 2
