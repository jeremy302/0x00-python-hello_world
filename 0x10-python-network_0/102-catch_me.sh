#!/bin/bash
# answer file
curl -s -X PUT -L -H 'Origin: School' -d "user_id=98" "0.0.0.0:5000/catch_me"
curl -s -H 'Origin: School' -L -d "user_id=98" "0.0.0.0:5000/catch_me" -X PUT -o /dev/null -w 'You got me!'
