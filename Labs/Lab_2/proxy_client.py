#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    # create socket, connect and receive data
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connection occurs here
        s.connect(addr)
        # sends all of the data
        s.sendall(payload.encode())
        # Shuts down connection once finished
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect((HOST, PORT))

if __name__ == '__main__':
    main()