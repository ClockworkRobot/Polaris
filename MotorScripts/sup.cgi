#!/bin/bash

gpio -g write 15 0

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
