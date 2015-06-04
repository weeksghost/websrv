import socket

HOST, PORT = '', 7777

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

count = 0
while True:
    client_connection, client_address = listen_socket.accept()
    client_connection.recv(1024)
    count += 1
    print(count)

    http_response = """\
HTTP/1.1 200 OK

Noice!
"""
    client_connection.sendall(http_response)
    client_connection.close()
