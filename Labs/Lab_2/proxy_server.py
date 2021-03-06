#!/usr/bin/env python3
import socket, time, sys

# Listen for hosts
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting ...')
        sys.exit()

    print(f'IP address of {host} is {remote_ip}')
    return remote_ip

def main():
    external_host = 'www.google.com'
    external_port = 80
    
    # TCP socket being created
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")

        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # binds HOST and PORT
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            # connect proxy_start
            conn, addr = proxy_start.accept()
            print("Connected by ", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print(f"Connecting to {external_host}")
                remote_ip = get_remote_ip(external_host)

                # connect proxy_end
                proxy_end.connect((remote_ip, external_port))

                # gets data from host
                send_full_data = conn.recv(BUFFER_SIZE)
                print(f'Sending received data {send_full_data} to Google')
                proxy_end.sendall(send_full_data)

                # shutdown proxy
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                print(f'Sending received data {data} to client')

                # sends connect data to local host
                conn.send(data)

            conn.close()

if __name__ == '__main__':
    main()
