import socket


def tcp_server():
    feeding_success = set()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 54321))
    server_socket.listen(5)
    print("TCP сервер запущен и ожидает соединений")

    while True:
        conn, addr = server_socket.accept()
        data = conn.recv(1024).decode().strip()
        
        responses = []
        for user_id in data.split("~"):
            if user_id:
                if user_id in feeding_success:
                    responses.append("Tolerated by the Cat")
                else:
                    responses.append("Scratched by the Cat")
        
        conn.send("".join(responses).encode())
        conn.close()
    


if __name__ == "__main__":

    tcp_server()