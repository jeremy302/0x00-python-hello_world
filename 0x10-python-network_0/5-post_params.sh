#!/bin/bash
# sends POST request with parameters
curl -s -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
