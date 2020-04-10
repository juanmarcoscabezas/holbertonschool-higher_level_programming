#!/bin/bash
# displays only the status code of the response.
curl -si -X GET -o /dev/null -w "%{http_code}" "$1"
