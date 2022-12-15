#!/bin/bash
# posts json
curl -s --data "$(cat "$2")" -H 'Content-Type: application/json' -H 'Accept: application/json' "$1"
