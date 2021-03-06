import socket
import termcolor
import colorama


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print('Ok')

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print('Server is up.')
            s.close()
        except ConnectionRefusedError:
            print('Could not connect to the server.')

    def __str__(self):
        return 'Connection to server at ' + self.ip + ', PORT : ' + str(self.port)

    def talk(self, msg):
        colorama.init(strip='False')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print(termcolor.colored('To server: ' + msg, 'blue'))
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode("utf-8")
        print('From server: ', end="")
        print(termcolor.colored(response, 'yellow'))
        # Close the socket
        s.close()
        # Return the response
        return 'From server: ' + response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print('To server:', colored(msg, 'blue'))
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        print('From server: ', colored(response, 'green'))



