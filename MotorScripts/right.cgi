#!/bin/bash

gpio -g write 23 0
gpio -g write 23 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
