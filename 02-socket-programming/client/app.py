from argparse import ArgumentParser
from socket import socket, AF_INET, SOCK_STREAM, gethostname

DEFAULT_VALUES = {
    "IP_ADDRESS": "127.0.0.1",
    "PORT": 8000,
    "FILE_NAME": "index.html",
    "MAX_CONNECTIONS": 5,
    "BUFF_SIZE": 4096,
}


# function for creating a client socket
def create_client_socket(ipaddr: str, port: int) -> socket:
    # create a socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # connect to the server
    client_socket.connect((ipaddr, port))

    # return the socket
    return client_socket


# function for parsing the arguments
def parse_arguments() -> tuple[str, int, str]:
    parser = ArgumentParser(
        prog="socket-prgramming-client",
        description="Simple socket programming client",
    )

    # get first argument as a ip address
    parser.add_argument("ipaddr", type=str, help="IP address")

    # get second argument as a port number
    parser.add_argument("port", type=int, help="Port number")

    # third argument as a file location
    parser.add_argument("filename", type=str, help="File location")

    # set default values to each parameters
    parser.set_defaults(
        ipaddr=DEFAULT_VALUES["IP_ADDRESS"],
        port=DEFAULT_VALUES["PORT"],
        filename=DEFAULT_VALUES["FILE_NAME"],
    )

    # parse the arguments and return them as results
    args = parser.parse_args()
    return args.ipaddr, args.port, args.filename


# function for receiving all the data from the socket using buffer
def recvall(socket: socket) -> bytes:
    data = b""
    while True:
        part = socket.recv(DEFAULT_VALUES["BUFF_SIZE"])
        data += part
        if len(part) < DEFAULT_VALUES["BUFF_SIZE"]:
            break
    return data


def http_response_parser(response: str) -> str:
    # extract html files from the response
    return response.split("<!DOCTYPE html>")[1]


def send_request(client_socket: socket, request: str) -> str:
    try:
        client_socket.sendall(request.encode("utf-8"))
        response = recvall(client_socket).decode("utf-8")

        # if the response status is 404, stop send and throw an exception
        if "404 Not Found" in response:
            raise FileNotFoundError("404 Not Found")

        # if the response status code is 20* but the response is incomplete, send request again
        if not "<!DOCTYPE html>" in response:
            print("incomplete response, send request again")
            return send_request(client_socket, request)

        return response

    except Exception as e:
        raise e


# entrypoint
def main():
    try:
        # parse the input from cli
        ipaddr, port, filename = parse_arguments()

        # print the ip address, port number, and file name
        print(
            f"[socket init from clinet]\n- ipaddr: {ipaddr}\n- port: {port}\n- file_loc: {filename}"
        )

        # print the hostname, port number, and ip adress
        print("\n---waiting for incoming connections---\n")

        # create a client socket
        client_socket = create_client_socket(ipaddr, port)

        # send a HTTP request to the server
        request = f"GET /{filename} HTTP/1.1\r\nHost: {ipaddr}:{port}\r\nConnection: close\r\n\r\n"
        response = send_request(client_socket, request)

        # print the response
        print("\n---response from the server---\n")
        print(response)

        # parse the response and extract html files from it
        html_response = http_response_parser(response)

        # save the html_respone to the file
        with open(filename, "w") as f:
            f.write(html_response)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close the client socket
        client_socket.close()


main()
