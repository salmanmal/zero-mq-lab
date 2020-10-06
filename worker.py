import zmq
import math
import time


context =zmq.Context()
        # Define the socket using the "Context"
sock=context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5557")

context2 =zmq.Context()
dashboard=context2.socket(zmq.PUSH)
dashboard.connect("tcp://127.0.0.1:3000")
# Run a simple "Echo" Server
while True:
    # ZeroMQ Context
    message=sock.recv()
    message=message.decode()
    if message:
        reply_msg="Square root of {} = {}".format(message,math.sqrt(int(message)))
        print(reply_msg)
        dashboard.send(reply_msg.encode())
    
    
    


    
    
    
    
    