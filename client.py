import socket

def feed_cat(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.sendto(message.encode(), ("localhost", 12345))
    response, _ = sock.recvfrom(1024)
    sock.close()
    return response.decode()

def pet_cat(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect(("localhost", 54321))
    sock.sendall(message.encode())
    response = sock.recv(1024)
    sock.close()
    return response.decode()