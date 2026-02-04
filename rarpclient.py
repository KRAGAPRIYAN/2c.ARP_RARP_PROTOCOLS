import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 6000

client.connect((host, port))

mac = input("Enter MAC Address: ")

client.send(mac.encode())

ip = client.recv(1024).decode()

print("IP Address:", ip)

client.close()
