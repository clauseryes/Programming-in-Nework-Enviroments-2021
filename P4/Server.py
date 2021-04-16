import socket
import pathlib


IP = "127.0.0.1"
PORT = 8080
FOLDER = './html/'

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def process_client(s):

    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    req_line = lines[0]
    path_name = req_line.split(' ')[1]

    print("Request line: ", end="")
    print(req_line)

    body = """ 
         """

    status_line = "HTTP/1.1 200 OK\n"

    header = "Content-Type: text/plain\n"

    if path_name == "/":
        body = read_html_file(FOLDER + 'index.html')

    elif "/info/" in path_name:
        try:
            body = read_html_file(FOLDER + path_name.split('/')[-1] + '.html')
        except FileNotFoundError:
            body = read_html_file(FOLDER + "error.html")

    header += f"Content-Length: {len(body)}\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())



ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()