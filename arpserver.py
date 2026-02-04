import socket

arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000

server.bind((host, port))
server.listen(1)

print("ARP Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to client:", addr)

ip_address = conn.recv(1024).decode()
print("Received IP:", ip_address)

mac_address = arp_table.get(ip_address, "IP Address not found in ARP Table")

conn.send(mac_address.encode())

conn.close()
server.close()
