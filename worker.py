import zmq
import math


# ZeroMQ Context
context =zmq.Context()


# Define the socket using the "Context"
sock=context.socket(zmq.PULL)
sock.bind("tcp://127.0.0.1:3001")


context2 =zmq.Context()
dashboard=context2.socket(zmq.PUSH)
dashboard.connect("tcp://127.0.0.1:3000")

# Run a simple "Echo" Server
while True:
    message=sock.recv()
    message=message.decode()
    reply_msg="Square root of {} = {}".format(message,math.sqrt(int(message)))
    dashboard.send(reply_msg.encode())
    print(reply_msg)