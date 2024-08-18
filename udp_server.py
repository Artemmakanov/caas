from collections import defaultdict
from datetime import datetime

import socket
import os
import json

CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE'))


def udp_server():
    STATS = {
        'feed': defaultdict(list),
        'pet': defaultdict(list)
    }
    with open('data/log.json', 'w') as f:
        json.dump(STATS, f)

    cat_preferences = {"Milk", "Meat"} 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 12345))
    print("UDP сервер запущен и ожидает соединений")

    while True:

        data, addr = server_socket.recvfrom(CHUNK_SIZE)
        message = data.decode().strip()
        message, fragment_number = message.split('~')
        while fragment_number:
            
            response = f"The Cat is amused by #{fragment_number}"
            server_socket.sendto(response.encode(), addr)

            data, addr = server_socket.recvfrom(CHUNK_SIZE)
            message_chunk = data.decode().strip()
            message_chunk, fragment_number = message_chunk.split('~')
            message += message_chunk
            
        user_id, food = message.split(" - ")
        response = "Eaten by the Cat" if food in cat_preferences else "Ignored by the Cat"
        STATS['feed'][user_id].append({
            'success': True if food in cat_preferences else False,
            'time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
        
        with open('data/log.json', 'w') as f:
            json.dump(STATS, f)
            
        server_socket.sendto(response.encode(), addr)


if __name__ == "__main__":

    udp_server()
