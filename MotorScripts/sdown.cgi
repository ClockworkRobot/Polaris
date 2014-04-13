#!/bin/bash

gpio -g write 14 0

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
