#!/usr/bin/python3
import urllib

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    print(res.read().decode())
