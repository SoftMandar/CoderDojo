import socket
import os
import struct

class FTPClient(object):

    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FILENAME='mata10'
    def __init__(self, server_address,reuseAddr=True):
        self.server_address = server_address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if reuseAddr:
            self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    def start_client(self):
        try:
            self.client_socket.connect(self.server_address)
            print("[*] Just connected at {}:{}".format(self.server_address[0], self.server_address[1]))
            self.download_file(FTPClient.FILENAME)
        except OSError:
            print("[*] Couldn`t connect.")

    def download_file(self, filename):
        with open(filename,'wb') as self.f:
            print("file opened...")
            while True:
                print("reciving data...")
                self.data = self.client_socket.recv(1024)
                self.file_size= os.path.getsize(self.data)
                self.unpacker=struct.Struct('I')
                self.unpacker_data=self.unpacker.unpack(self.file_size)[0]
                if not self.unpacker_data:
                    break
                self.f.write(self.unpacker_data)
        self.f.close()
        self.client_socket.close()

if __name__ == "__main__":
    ftp = FTPClient(("127.0.0.1", 8085))
    ftp.start_client()