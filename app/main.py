import socket  # noqa: F401
import threading

def handle_client(client_socket, addr):
    while True:
        req = client_socket.recv(1024)
        data = req.decode()
        if "ping" in data.lower():
            client_socket.send(b'+PONG\r\n')


def main():
    print("Starting socket server")
    try:    
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        server_socket.listen()

        while True:
            client_socket, client_address = server_socket.accept() # wait for client
            print(f"Connection established wih {client_address}")

            thread = threading.Thread(target=handle_client, args = (client_socket, client_address))
            thread.start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
