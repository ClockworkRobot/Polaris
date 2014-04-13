#!/bin/bash

gpio -g write 14 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
