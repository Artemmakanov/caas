import socket

def udp_server():
    cat_preferences = {"Milk", "Meat"} 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 12345))
    print("UDP сервер запущен и ожидает соединений")

    while True:

        data, addr = server_socket.recvfrom(4)
        message = data.decode().strip()
        print(message)
        message, fragment_number = message.split('~')
        while fragment_number:
            
            response = f"The Cat is amused by #{fragment_number}"
            server_socket.sendto(response.encode(), addr)

            data, addr = server_socket.recvfrom(4)
            message_chunk = data.decode().strip()
            message_chunk, fragment_number = message_chunk.split('~')
            message += message_chunk
            
        user_id, food = message.split(" - ")
        response = "Eaten by the Cat" if food in cat_preferences else "Ignored by the Cat"
        server_socket.sendto(response.encode(), addr)


if __name__ == "__main__":

    udp_server()
