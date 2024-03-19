import socket

# IP address and port to listen on
host = '0.0.0.0'  # Listen on all available interfaces
port = 12345

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
sock.bind((host, port))
while True:
    # Receive data
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from {addr}: {data.decode()}")

# Close the socket
sock.close()
