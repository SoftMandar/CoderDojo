import socket
import subprocess

def handle_client(client_socket):

    MAX_RECV_BUFFER = 1024

    allowed_commands = ["ls, cd, ls -l"]

    recv_size = 1
    while recv_size:

        data_buffer = client_socket.recv(MAX_RECV_BUFFER)
        command = data_buffer.decode("utf-8")

        if not data_buffer:
            print("Client just disconected")
            break

        recv_size = len(data_buffer)

        if command in allowed_commands:
            response = run_command(commad)
            client_socket.send(response.encode("utf-8"))
        data_buffer = ""

def init_server(server_address, reuseAddr=True):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(server_address)
    except socket.error as serr:
        print(str(serr))

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if hasattr(socket, "SO_REUSEPORT"):
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT)

    server_socket.listen(5)

    print("Server listen at {}:{}".format(server_address[0], server_address[1]))

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            print("Client has connected {}:{}".format(client_address[0], client_address[1]))

            handle_client(client_socket)

    except KeyboardInterrupt as kerr:
        print("Server is closing...")
        client_socket.close()
        server_socket.close()

def run_command(commad):
    try:
        output = subprocess.check_output(commad, stderr=subprocess.STDOUT, shell=True)
    except OSError as oserr:
        return output


if __name__ == "__main__":
    init_server(("127.0.0.1",8080))
