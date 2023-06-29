import zmq
import json
import time
import requests

context = zmq.Context()

socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")

URL_API_CALL = "http://api.open-notify.org/iss-now.json"

def get_iss_location(url: str) -> dict:
    r = requests.get(url)

    if r.status_code == 200:
        r = r.json()

    else:
        r = {'message': 'fail'}

    return r


for request in range(10):
    response = get_iss_location(URL_API_CALL)

    socket.send_string(json.dumps(response))

    time.sleep(1)