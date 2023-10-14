from pathlib import Path

frame_name_pattern = "*.jpg"

# Detection
KERNEL_SIZE = 10
NUM_DETECTIONS = 3

# ZMQ
ZMQ_NEW_FILE_PUB_PORT = 8880

# General
LOG_DIRECTORY = Path("/tmp/logs")

# Camera 0
cam0_file_stream_path = Path("/tmp/frames/cam0_full")
cam0_preprocessing_stream_path = Path("/tmp/frames/cam0_split")

# Camera 1
cam1_file_stream_path = Path("/tmp/frames/cam1_full")
