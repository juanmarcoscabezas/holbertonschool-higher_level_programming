#!/bin/bash
# displays only the status code of the response.
curl -si -X GET --stderr - "$1" | grep "HTTP/1.0" | cut -b 10-12
