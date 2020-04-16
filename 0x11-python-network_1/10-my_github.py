#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/users/' + sys.argv[1]
    token = 'token ' + sys.argv[2]

    headers = {'Authorization': token}
    payload = {'Accept': 'application/vnd.github.v3+json'}

    r = requests.get(url, params=payload, headers=headers)
    try:
        body = r.json()
        if r.status_code >= 400:
            print('None')
        else:
            print('{}'.format(body['id']))
    except ValueError:
        print('Not a valid JSON')
