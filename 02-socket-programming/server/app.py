from socket import socket, AF_INET, SOCK_STREAM, gethostname
from argparse import ArgumentParser
from re import search as regexp_search

DEFAULT_VALUES = {"PORT": 8000, "DIR": ".", "MAX_CONNECTIONS": 1024, "BUFF_SIZE": 4096}


# custom exception for FileNotFoundError
class FileNotFoundCustomException(Exception):
    pass


# function for parsing the arguments
def parse_arguments() -> tuple[str, int]:
    parser = ArgumentParser(
        prog="socket-prgramming-server",
        description="Simple socket programming server",
    )

    # get first argument as a port number
    parser.add_argument("port", type=int, help="Port number")

    # and get second argument as a file location
    parser.add_argument("dir", type=str, help="Directory location")

    # set default value to 8000, the DEFAULT_PORT
    # set default value to cwd(current working directory), the DEFAULT_DIR
    parser.set_defaults(port=DEFAULT_VALUES["PORT"], dir=DEFAULT_VALUES["DIR"])

    # parse the arguments and return them as results
    args = parser.parse_args()
    return args.port, args.dir


# function for creating a socket
def create_socket(port: int) -> socket:
    # create a socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # bind the socket to the port
    server_socket.bind((gethostname(), port))

    # return the socket
    return server_socket


# function for receiving all the data from the socket using buffer
def recvall(socket: socket) -> bytes:
    data = b""
    while True:
        part = socket.recv(DEFAULT_VALUES["BUFF_SIZE"])
        data += part
        if len(part) < DEFAULT_VALUES["BUFF_SIZE"]:
            break
    return data


# function for parsing the request
# and extract the file name from the request
def request_parser(request: str) -> str:
    # extract file name from GET {file_name} HTTP/1.1
    # after "GET " and before "HTTP/1.1"
    # using regular expression
    return regexp_search(r"GET /(.*) HTTP/1.1", request).group(1)


# entrypoint
def main():
    # parse the input from cli
    port, dir = parse_arguments()

    # create a socket
    server_socket = create_socket(port)
    # listen for incoming connections
    server_socket.listen(DEFAULT_VALUES["MAX_CONNECTIONS"])

    # print the hostname, port number, and ip adress
    print(
        f"[socket init from server]\n- hostname: {gethostname()}\n- port: {port}\n- ipaddr: {server_socket.getsockname()}"
    )
    # print a message for waiting for incoming connections
    print("\nwaiting for incoming connections\n")
    print("\n----\n")

    try:
        # if the socket is successfully created, run these jobs
        # as a result of successfully socket creation,
        while True:
            # accept the incoming connection
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr} has been established)")

            try:
                # parse the client request
                decoded_request = recvall(client_socket).decode("utf-8")

                # print the request from the client
                print(f"Request from client: \n\n{decoded_request}")
                print("\n----\n")

                # get file name from the request
                file_name = request_parser(decoded_request)

                # open the file using the request
                try:
                    with open(f".{dir}/{file_name}", "rb") as file:
                        # send the response to the client
                        client_socket.send("HTTP/1.1 200 OK\n".encode("utf-8"))
                        client_socket.send(
                            "Content-Type: text/html\n\n".encode("utf-8")
                        )
                        # read the file and send it to the client
                        while True:
                            data = file.read(DEFAULT_VALUES["BUFF_SIZE"])
                            if not data:
                                break
                            client_socket.send(data)
                # if the file is not found, raise an error
                except FileNotFoundError:
                    raise FileNotFoundCustomException(f"File not found: {file_name}")
            # handle errors for network connection
            except FileNotFoundCustomException as e:
                print(e)
                client_socket.send("HTTP/1.1 404 Not Found\n\n".encode("utf-8"))
            finally:
                # close the client socket
                print("closing the client socket")
                client_socket.close()

    except Exception as e:
        print(e)
    finally:
        # close the server socket
        print("closing the server socket")
        server_socket.close()


main()
