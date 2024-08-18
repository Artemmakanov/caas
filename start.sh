#!/bin/bash


source .venv/bin/activate

export CHUNK_SIZE="400"

# python3 dns.py &
python3 udp_server.py &
python3 tcp_server.py &
python3 app.py