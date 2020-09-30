import zmq
import sys
import time

# ZeroMQ Context
context=zmq.Context()

# Define the socket using the "Context"
# Bind is server
sock=context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:3001")

# Send a "message" using the socket
for i in range(10):
    time.sleep(1)
    print(i)
    sock.send("{}".format(i).encode())

sock.close()