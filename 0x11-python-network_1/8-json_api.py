#!/usr/bin/python3
"""this script fetches https://intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://localhost:5000/search_user'
    payload = {'q': ''}
    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]
    r = requests.post(url, payload)
    try:
        body = r.json()
        if body:
            print('[{}] {}'.format(body['id'], body['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
