#!/bin/bash

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""

gpio -g write 7 0
sleep 7
gpio -g write 7 1
