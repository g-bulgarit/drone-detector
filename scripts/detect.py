import zmq
import json

from drone_detection.detection.find_by_correlation import find_anomalies
from drone_detection.configuration.config import (
    ZMQ_NEW_FILE_PUB_PORT,
    KERNEL_SIZE,
    NUM_DETECTIONS,
)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")
socket.subscribe("")

if __name__ == "__main__":
    # Load a model
    while True:
        path_str = socket.recv_string()
        recv_dict = json.loads(path_str)
        frame_path: str = recv_dict["path"]

        # Run batched inference on a list of images
        anomalies = find_anomalies(
            image_path=frame_path, kernel_size=KERNEL_SIZE, k=NUM_DETECTIONS
        )  # return a list of Results objects

        print(f"Found {len(anomalies)}!")
