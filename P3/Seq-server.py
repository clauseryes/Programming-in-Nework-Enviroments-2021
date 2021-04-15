import socket
import server_utils

list_sequences = ['ACCGTGGTGTAACGAAA', 'ATTTGCTGTCTCT', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print('Connection: ' + str(count_connections) + '. Client ip, port: ' + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    formatted_msg = server_utils.format_command(msg)
    #print(formatted_msg)
    formatted_msg = formatted_msg.split(' ')

    if len(formatted_msg) == 1:
        command = formatted_msg[0]
    else:
        command = formatted_msg[0]
        argument = formatted_msg[1]

    if command == 'PING':
        server_utils.ping(cs)
    elif command == 'GET':
        server_utils.get(cs, list_sequences, argument)
    elif command == 'INFO':
        server_utils.info(cs, argument)
    elif command == 'COMP':
        server_utils.comp(cs, argument)
    elif command == 'REV':
        server_utils.rev(cs, argument)
    elif command == 'GENE':
        server_utils.gene(cs, argument)
    else:
        response = 'Not available command.'
        cs.send(str(response).encode())
    cs.close()



