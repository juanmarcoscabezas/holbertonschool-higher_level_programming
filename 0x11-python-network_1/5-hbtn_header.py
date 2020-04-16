#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    headers = r.headers
    print(headers['X-Request-Id'])
