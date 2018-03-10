import socket
import struct

class FTPServer(object):

    def __init__(self, server_addr=None, backLog=10, setBlocking=False, reuseAddr=True):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if server_addr not None:
            self.server_address = "127.0.0.1"
        else:
            self.server_socket = socket.gethostbyname(socket.gethostname())

        try:
            self.server_socket.bind(self.server_socket)
        except socket.error:
            pass

        if setBlocking:
            self.server_socket.setblocking(0)

        if reuseAddr:
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.listen(backLog)
        self.active_server = True
        print("")

    def start_server(self):

        try:
            while self.active_server:
                pass
        except KeyboardInterrupt:
            self.shutdown_server()

    def shutdown_server(self):
        print("")
        self.active_server = False
        self.server_socket.close()

    def send_file(self, file_location, client_sock):
        pass
