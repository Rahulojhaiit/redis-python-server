import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen(2)

    client_socket, client_address = server_socket.accept() # wait for client
    print(f"Connection established wih {client_address}")

    data = client_socket.recv(2048)
    print(f"Received data: `{data.decode()}`")

    resp =  b'+PONG\r\n'
    client_socket.send(resp)
    data = client_socket.recv(2048)
    if data: 
        print(f"Received data: `{data.decode()}`")
        resp =  b'+PONG\r\n'
        client_socket.send(resp)

    client_socket.close()


if __name__ == "__main__":
    main()
