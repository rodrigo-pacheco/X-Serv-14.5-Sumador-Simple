#!/usr/bin/python3
"""
Simple HTTP Server: serves random URLs usign a hyperlink

Rodrigo Pacheco Martinez-Atienza
r.pachecom @ gsyc.es
SAT subject (Universidad Rey Juan Carlos)
"""

import socket
import calculadora

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print('Answering back...')

        received = str(recvSocket.recv(2048))
        info = str(received.split()[1])
        _, op1, operation, op2 = info.split("/")

        try:
            answer = calculadora.operaciones[operation](int(op1), int(op2))
        except KeyError:
            answer = 'Opción no encontrada. Pruebe: suma, resta, multiplica o divide'

        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body>" +
                        answer +
                        "</body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
