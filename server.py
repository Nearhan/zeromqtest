import zmq
import sys


PORT = '9001'
IP = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://%s:%s" % (IP, PORT))

while True:
    socket.send("Server message to client3")
    msg = socket.recv()
    print msg
