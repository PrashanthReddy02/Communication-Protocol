import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Server listening on port 8080")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        # Receive message from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message: {data}")

        # Send a response to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
