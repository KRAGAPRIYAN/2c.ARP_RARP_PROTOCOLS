import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000

client.connect((host, port))

ip = input("Enter IP Address: ")

client.send(ip.encode())

mac = client.recv(1024).decode()

print("MAC Address:", mac)

client.close()
