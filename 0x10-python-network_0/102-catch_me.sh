#!/bin/bash
# answer file
curl -s -X PUT -L --max-redirs -1 -H 'Origin: School' -d "user_id=98" "0.0.0.0:5000/catch_me"


# curl -v -s --no-keepalive --post301 --post302 --post303 -X PUT -L -H 'Origin: School' -d "user_id=98" "0.0.0.0:5000/catch_me"

# curl -v -s --no-keepalive --post301 --post302 --post303 -X PUT -L "0.0.0.0:5000/catch_me" -d "user_id=98"

# curl -s -H 'Origin: School' -L -d "user_id=98" "0.0.0.0:5000/catch_me" -X PUT
