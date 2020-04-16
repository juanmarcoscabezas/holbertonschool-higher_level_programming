#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers['X-Request-Id']
        print(request_id)
