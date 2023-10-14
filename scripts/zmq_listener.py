import zmq
import json

from drone_detection.configuration.config import ZMQ_NEW_FILE_PUB_PORT

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")
    socket.subscribe("")

    while True:
        path_str = socket.recv_string()
        recv_dict = json.loads(path_str)
        print(recv_dict)
