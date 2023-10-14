from pathlib import Path

frame_name_pattern = "*.jpg"

# Camera capture parameters
RESOLUTION: tuple[int, int] = (2592, 1944)
FPS: int = 5

# Detection
KERNEL_SIZE = 10
NUM_DETECTIONS = 3

# ZMQ
ZMQ_NEW_FILE_PUB_PORT = 8880

# General
LOG_DIRECTORY = Path("/tmp/logs")

# Camera 0
CAM0_FILE_STREAM_PATH = Path("/tmp/frames/cam0_full")
CAM0_PREPROCESSING_STREAM_PATH = Path("/tmp/frames/cam0_split")

# Camera 1
CAM1_FILE_STREAM_PATH = Path("/tmp/frames/cam1_full")
