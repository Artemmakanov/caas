import socket
import os
import random
import json
from collections import defaultdict
from datetime import datetime

CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE'))

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("0.0.0.0", 54321))
    server_socket.listen(5)
    print("TCP сервер запущен и ожидает соединений")
    tired = False

    while True:
        message = ''
        conn, addr = server_socket.accept()
        message_chunk = conn.recv(CHUNK_SIZE).decode('utf-8').strip()
        message += message_chunk
        # print(message)
        
        while message_chunk and message_chunk[-1] != '~':
            conn.close()
            conn, addr = server_socket.accept()
            message_chunk = conn.recv(CHUNK_SIZE).decode('utf-8').strip()
            message += message_chunk
            # print(message)
        
        with open('data/log.json', 'r') as f:
            STATS = json.load(f)
            STATS['feed'] = defaultdict(list, STATS['feed'])
            STATS['pet'] = defaultdict(list, STATS['pet'])

        response = ''
        for user_id in message.split('~')[:-1]:
            tolerated = any(dct['success'] for dct in STATS['feed'][user_id])
            if random.randint(0, 5) == 5:
                print('Кот устал. Сервер закрывается!')
                tired = True

            STATS['pet'][user_id].append({
                'success': tolerated and not tired,
                'time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
            
            with open('data/log.json', 'w') as f:
                json.dump(STATS, f)

            response += 'Tolerated by the Cat' if tolerated and not tired else 'Scratched by the Cat'
        
        conn.sendall(response.encode())
        conn.close()
        if tired:
            break

if __name__ == "__main__":

    tcp_server()