import socket

def udp_server():
    cat_preferences = {"Milk", "Meat"}  # Пример предпочтений кота
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 12345))
    print("UDP сервер запущен и ожидает соединений")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode().strip()
        
        if "~" in message:
            user_id, food = message.split(" - ")
            food = food.replace("~", "")
            response = "Eaten by the Cat" if food in cat_preferences else "Ignored by the Cat"
        else:
            fragment_number = message[-1]
            response = f"The Cat is amused by #{fragment_number}"

        server_socket.sendto(response.encode(), addr)


if __name__ == "__main__":

    udp_server()
