import zmq
import sys

# ZeroMQ Context
context=zmq.Context()

# Define the socket using the "Context"
sock=context.socket(zmq.PUSH)
sock.connect("tcp://127.0.0.1:3001")

# Send a "message" using the socket
for i in range(10001):
    sock.send("{}".format(i).encode())

# print(sock.recv().decode())