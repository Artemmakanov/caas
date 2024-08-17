source .venv/bin/activate
python3 udp_server.py &
python3 tcp_server.py &
python3 app.py &
wait