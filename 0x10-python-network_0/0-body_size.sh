#!/bin/bash
# DIsplays the size of the body in the response
curl -si -X GET --stderr - "$1" | grep "Content-Length" | cut -d " " -f 2
