#!/bin/bash

while true
do

pgrep -f "uvicorn" >/dev/null

if [ $? -ne 0 ]; then

cd ~/HUDA_DESKTOP_APP

nohup uvicorn api.server:app \
--host 0.0.0.0 \
--port 8000 >/dev/null 2>&1 &

fi

sleep 20

done
