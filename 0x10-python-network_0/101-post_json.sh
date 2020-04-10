#!/bin/bash
# displays only the status code of the response.
curl -s -H "Content-Type: application/json" -X POST "$1" -T "$2"
