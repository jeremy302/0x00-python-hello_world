#!/usr/bin/python3
# json api
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    letter = (sys.argv[2:] or [''])[0]
    res = requests.post(url, params={'q': letter})
    res_json = {}
    try:
        res_json = res.json()
        if 'id' not in res_json and 'name' not in res_json:
            print('No result')
        else:
            print(f'[{res_json.get("id")}] {res_json.get("name")}')
    except Exception:
        print('Not a valid JSON')
        
