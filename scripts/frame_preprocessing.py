import zmq
import json
from pathlib import Path

from drone_detection.image_processing.preprocessing import preprocess_frame
from drone_detection.configuration.config import (
    ZMQ_NEW_FILE_PUB_PORT,
    CAM0_PREPROCESSING_STREAM_PATH,
)


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")
    socket.subscribe("")
    output_dir = Path(CAM0_PREPROCESSING_STREAM_PATH)
    output_dir.mkdir(parents=True, exist_ok=True)

    while True:
        path_str = socket.recv_string()
        recv_dict = json.loads(path_str)
        frame_path = Path(recv_dict["path"])
        preprocess_frame(frame_path=frame_path, output_dir=output_dir)
        print(recv_dict)
