#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -H "Origin:HolbertonSchool" -L -F "user_id=98" 0.0.0.0:5000/catch_me
