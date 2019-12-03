import socket
import sys
import struct

def loggerProcess(name):
    print('i am the process', name)
# Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    sock.sendto(b'ok to receive', server_address)
        # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(struct.unpack('<1f',data)))
    print('closing socket')
    sock.close()
