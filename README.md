# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.

## Date: 02/02/2026
## Roll.No: 212225040323

## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
P
## PROGRAM - ARP

arpserver.py

```
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
```

arpclient.py

```
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
```

## OUPUT - ARP

Server-Side

![alt text](<Screenshot 2026-02-04 093134.png>)

Client-Side

![alt text](<Screenshot 2026-02-04 093204.png>)

Execution

![alt text](<Screenshot 2026-02-04 093118.png>)

## PROGRAM - RARP

rarpserver.py

```
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
```

rarpclient.py

```
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
```

## OUPUT -RARP

Server-Side

![alt text](<Screenshot 2026-02-04 093346.png>)

Client-Side

![alt text](<Screenshot 2026-02-04 093402.png>)

Execution

![alt text](<Screenshot 2026-02-04 093328.png>)

## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
