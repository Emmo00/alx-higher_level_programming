#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sIL -X OPTIONS "$1" | grep -iF "allow" | cut -b 8-
