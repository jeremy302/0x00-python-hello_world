#!/bin/bash
# sends DELETE request
curl -s -i -L -X OPTIONS "$1" | grep -Po '(?<=Allow:\s).+'
