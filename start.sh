#!/bin/bash


source .venv/bin/activate

export CHUNK_SIZE="4"

python3 udp_server.py &
python3 tcp_server.py &
python3 app.py