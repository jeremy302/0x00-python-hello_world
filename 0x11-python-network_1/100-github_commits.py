#!/usr/bin/python3
''' github commit api '''
import sys
import requests

if __name__ == '__main__':
    repo, owner = sys.argv[1:3]
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits',
                       auth=(user, passwd), params={'per_page': 10})
    for item in res.json():
        commit = item['commit']
        sha = item['sha']
        author = commit['author']['name']
        print(f'{sha}: {author}')
