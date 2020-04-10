#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -X PUT -H "Origin:HolbertonSchool" "$1"
