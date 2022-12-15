#!/bin/bash
# answer file
curl -s -X PUT -L --max-redirs -1 -H 'Origin: School' -d "user_id=98" "0.0.0.0:5000/catch_me"
