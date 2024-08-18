import socket
from dnslib import DNSRecord, QTYPE, CLASS

def resolve_srv(service, protocol, domain):
    qname = f"_{service}._{protocol}.{domain}."
    qtype = "SRV"  # Передаем тип в виде строки, как ожидается
    qclass = "IN"  # Передаем класс в виде строки

    q = DNSRecord.question(qname, qtype=qtype, qclass=qclass)
    
    # Здесь предполагается, что DNS-сервер работает на localhost
    response = q.send("localhost", 53, tcp=True)
    dns_response = DNSRecord.parse(response)
    srv_record = dns_response.rr[0].rdata

    return str(srv_record.target), srv_record.port

def feed_cat(message):
    target, port = resolve_srv("feed", "udp", "catdomain.local")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (target, port))
    response, _ = sock.recvfrom(1024)
    sock.close()
    return response.decode()

def pet_cat(message):
    target, port = resolve_srv("pet", "tcp", "catdomain.local")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, port))
    sock.sendall(message.encode())
    response = sock.recv(1024)
    sock.close()
    return response.decode()
