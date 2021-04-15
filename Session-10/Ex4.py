import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
count_connections = 0
ls.listen()

print("The server is configured!")
client_address_list = []

while True:

    print("Waiting for Clients to connect.")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print('Connection: ' + str(count_connections) + '. Client ip, port: ' + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    print("A client has connected to the server!")

    msg_raw = cs.recv(2048)

    msg = msg_raw.decode()

    print(f"Message received: {msg}")

    response = 'ECHO: ' + msg

    cs.send(str(response).encode())

    cs.close()

    if count_connections == 5:
        for i in range(0, len(client_address_list)):
            print('Client ' + str(i) + '. Client ip, port: ' + str(client_address_list[i]))
        exit(0)