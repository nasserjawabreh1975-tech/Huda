#!/bin/bash

while true
do

echo "=========================" >> \
~/HUDA_DESKTOP_APP/logs/runtime.log

date >> \
~/HUDA_DESKTOP_APP/logs/runtime.log

free -h >> \
~/HUDA_DESKTOP_APP/logs/runtime.log

df -h >> \
~/HUDA_DESKTOP_APP/logs/runtime.log

sleep 60

done
