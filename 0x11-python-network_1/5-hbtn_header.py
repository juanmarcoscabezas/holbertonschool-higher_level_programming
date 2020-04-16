#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    headers = r.headers
    print(headers.get('X-Request-Id'))
