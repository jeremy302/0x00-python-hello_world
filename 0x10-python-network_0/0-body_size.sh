#!/bin/bash
# returns body length
curl -s -o /dev/null -w '%{size_download}\n' "$1"
