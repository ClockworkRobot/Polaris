#!/bin/bash

for ((n=0;n<10;n++)); do ./up.cgi; done
for ((n=0;n<10;n++)); do ./down.cgi; done
for ((n=0;n<10;n++)); do ./left.cgi; done
for ((n=0;n<10;n++)); do ./right.cgi; done


echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
