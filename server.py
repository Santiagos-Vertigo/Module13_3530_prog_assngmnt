import socket
import random
import sys
import os

def main():
    host = sys.argv[1] if len(sys.argv) > 1 else socket.gethostname()
    port = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv('SERVER_PORT', 8008))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    # print(f"\nUNIVERSITY OF NORTH TEXAS")
    # print(f"\nCSCE 3530-400")
    # print(f"\nModule 13: Network Programming Assignment")
    # print(f"\nDiego Narvaez")
    # print(f"\nEUID: 11512562 / dn0240")
    # print(f"\n[server] : ready to accept data on {host}:{port}\n")
    
    
    
    print("\nUNIVERSITY OF NORTH TEXAS\n")
          
          
    print("CSCE 3530-400\n"
          "Module 13: Network Programming Assignment\n")
          
          
    print("Diego Narvaez\n"
          "EUID: 11512562 / dn0240\n")
          
    print(f"[server] : ready to accept data on {host}:{port}\n")
    

    while True:
        data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        message = data.decode()
        print(f"[client] : {message}")

        if random.random() > 0.3:  # the 70% variable
            server_socket.sendto(b'PONG', addr)
            print("[server] : PONG")
        else:
            print("[server] : packet dropped")

if __name__ == "__main__":
    main()
