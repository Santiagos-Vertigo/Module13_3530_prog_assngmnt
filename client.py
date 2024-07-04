import socket
import sys

def main():
    host = sys.argv[1] if len(sys.argv) > 1 else socket.gethostname()
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8008

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout of 1 second for receiving a response
    client_socket.settimeout(1)

    for i in range(1, 11):
        message = b'PING'
        client_socket.sendto(message, (host, port))
        print(f"{i} : sent PING...", end=' ')

        try:
            data, server = client_socket.recvfrom(1024)
            print(f"received {data}")
        except socket.timeout:
            print("Timed Out")

    client_socket.close()

if __name__ == "__main__":
    main()

