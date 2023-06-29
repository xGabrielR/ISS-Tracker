import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    message = json.loads(message)

    print(f"Received Request: {message}")

    time.sleep(1)