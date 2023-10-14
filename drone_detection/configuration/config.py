from pathlib import Path

frame_name_pattern = "*.jpg"

# ZMQ
ZMQ_NEW_FILE_PUB_PORT = 8880

# Camera 0
cam0_file_stream_path = Path("/tmp/logs/cam0")
cam0_logfile = Path("/tmp/cam0_filewd.log")

# Camera 1
cam1_file_stream_path = Path("/tmp/cam1")
cam1_logfile = Path("/tmp/logs/cam1_filewd.log")
