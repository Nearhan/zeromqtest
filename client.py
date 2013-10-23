import zmq
import sys

PORT = '9001'
IP = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://%s:%s" % (IP, PORT))

while True:
    msg = socket.recv()
    print msg
    socket.send("client message to server1")
    socket.send("client message to server2")
