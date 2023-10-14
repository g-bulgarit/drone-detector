import zmq
import json
import cv2
from pathlib import Path

from drone_detection.configuration.config import ZMQ_NEW_FILE_PUB_PORT


def preprocess_frame(frame_path: Path, output_dir: Path):
    image_frame_count = Path(frame_path).stem
    image = cv2.imread(str(frame_path))
    h, w, _ = image.shape
    tilex = w // 2
    tiley = h // 2
    tile_counter = 0
    for y in range(0, h, tiley):
        for x in range(0, w, tilex):
            output_filename = f"{output_dir}/{image_frame_count}_{tile_counter}.jpg"
            tile = image[y : y + tiley, x : x + tilex]
            cv2.imwrite(filename=output_filename, img=tile)
            tile_counter += 1


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")
    socket.subscribe("")
    output_dir = Path(r"D:\Code\drone-detection\split_frames")

    while True:
        path_str = socket.recv_string()
        recv_dict = json.loads(path_str)
        frame_path = Path(recv_dict["path"])
        preprocess_frame(frame_path=frame_path, output_dir=output_dir)
        print(recv_dict)
