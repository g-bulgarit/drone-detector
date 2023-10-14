from ultralytics import YOLO
import zmq
import json

from drone_detection.detection.utils import is_drone
from drone_detection.configuration.config import ZMQ_NEW_FILE_PUB_PORT

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")
socket.subscribe("")

if __name__ == "__main__":
    # Load a model
    model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model

    while True:
        path_str = socket.recv_string()
        recv_dict = json.loads(path_str)
        frame_path: str = recv_dict["path"]

        # Run batched inference on a list of images
        results = model(frame_path)  # return a list of Results objects
        config = dict(monitored_classes_ids=[5], detection_confidence_threshold=0.8)
        detection_result = is_drone(results[0], config=config)
        print(f"Drone detected? {detection_result}")
