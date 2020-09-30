import zmq
import math
import time


# Run a simple "Echo" Server
while True:
    # ZeroMQ Context
    try :
        context =zmq.Context()
        # Define the socket using the "Context"
        sock=context.socket(zmq.PULL)
        sock.connect("tcp://127.0.0.1:3001")
        message=sock.recv()
        sock.close()
        message=message.decode()
        if message:
            context2 =zmq.Context()
            dashboard=context2.socket(zmq.PUSH)
            dashboard.bind("tcp://127.0.0.1:3000")
            reply_msg="Square root of {} = {}".format(message,math.sqrt(int(message)))
            print(reply_msg)
            dashboard.send(reply_msg.encode())
            dashboard.close()
    except:
        print("connection busy retry")
    time.sleep(3)


    
    
    
    
    