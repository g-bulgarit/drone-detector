from pathlib import Path

frame_name_pattern = "*.jpg"

# ZMQ
ZMQ_NEW_FILE_PUB_PORT = 8880

log_directory = Path("/tmp/logs")

# Camera 0
cam0_file_stream_path = Path("/tmp/frames/cam0_full")
cam0_preprocessing_stream_path = Path("/tmp/frames/cam0_split")

# Camera 1
cam1_file_stream_path = Path("/tmp/frames/cam1_full")
