#!/bin/bash
# displays all HTTP methods the server will accept.
curl -si -X GET --stderr - "$1" | grep "Allow: " | cut -b 8-
