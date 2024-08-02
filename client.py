import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    while True:
        # Send a message to the server
        message = input("Enter your message: ")
        client_socket.send(message.encode())

        # Receive a response from the server
        response = client_socket.recv(1024).decode()
        if not response:
            break
        print(f"Message from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
