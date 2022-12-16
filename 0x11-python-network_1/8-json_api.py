#!/usr/bin/python3
''' json api '''
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = (sys.argv[1:] or [''])[0]
    res = requests.post(url, data={'q': letter})
    res_json = {}
    try:
        res_json = res.json()
        if 'id' not in res_json and 'name' not in res_json:
            print('No result')
        else:
            print(f'[{res_json.get("id")}] {res_json.get("name")}')
    except Exception:
        print('Not a valid JSON')
