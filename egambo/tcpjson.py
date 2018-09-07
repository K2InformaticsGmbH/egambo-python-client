import socket
import ssl
import json
import datetime

class TcpJson:
    def __init__(self, host, port, is_ssl):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if is_ssl:
            print(timestamp() + "SSL connecting to " + host + ":" + str(port))
            self._sock = ssl.wrap_socket(self._sock)
        else:
            print("connecting to " + host + ":" + str(port))

        self._sock.connect((host,port))

    def __del__(self):
        self._sock.close()

    def send(self, jsn):
        """ TX JSON with unsigned 4-bytes length header. """
        tx = json.dumps(jsn).encode('utf-8')            # serialize to utf-8 bytes
        txlen = len(tx)                                 # calculate payload length
        tx = txlen.to_bytes(4, byteorder = 'big') + tx  # prepend 32 bit length header
        print(timestamp() + 'TXRAW  : ', end='')
        print(tx, flush=True)
        self._sock.send(tx)

    def recv(self):
        """ RX JSON with unsigned 4-bytes length header. """
        data = self._sock.recv(4) # receive only 4 bytes first (32 bit length header)
        rxlen = int.from_bytes(data, byteorder='big') # convert to integer
        print(rxlen)
        rx = self._sock.recv(rxlen)      # receive a full json binary and decode to string
        jsn = json.loads(rx.decode())   # decode json to python object
        print(timestamp() + 'RXRAW  : ', end='')
        print(data + rx)
        return jsn

def timestamp():
    """ Returns a formatted timestamp. """
    return '{:%Y-%m-%d %H:%M:%S} '.format(datetime.datetime.now())
