#!/bin/bash
# Display the length of the response
curl -sI "$1" | grep -oP '(?<=Content-Length: )[0-9]+'
