#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    r = requests.post(url, data)
    print(r.text)
