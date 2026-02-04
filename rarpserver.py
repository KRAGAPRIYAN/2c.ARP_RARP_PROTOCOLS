import socket

rarp_table = {
    "AA:BB:CC:DD:EE:01": "192.168.1.1",
    "AA:BB:CC:DD:EE:02": "192.168.1.2",
    "AA:BB:CC:DD:EE:03": "192.168.1.3"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 6000

server.bind((host, port))
server.listen(1)

print("RARP Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to client:", addr)

mac_address = conn.recv(1024).decode()
print("Received MAC:", mac_address)

ip_address = rarp_table.get(mac_address, "MAC Address not found in RARP Table")

conn.send(ip_address.encode())

conn.close()
server.close()
