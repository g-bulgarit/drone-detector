import sys
import zmq
from drone_detection.configuration.config import (
    frame_name_pattern,
    ZMQ_NEW_FILE_PUB_PORT,
    cam0_file_stream_path,
    LOG_DIRECTORY,
)
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileMovedEvent
from drone_detection.communication.messages import NewFileFoundMsg
import json


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")


def watch_and_notify(working_dir: Path, name: str) -> Observer:
    file_handler = logging.FileHandler(filename=f"{LOG_DIRECTORY}/filemon_{name}.log")
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    logging.basicConfig(
        format="[%(asctime)s] | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[file_handler, stdout_handler],
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.debug(f"Started logging new files at {working_dir}")

    # Nest closure to retain specific parameters in thread
    def on_moved_event_handler(event: FileMovedEvent) -> None:
        # Frames are saved in a temp file and then moved to a new file without a temp
        # extension. We want to capture this event.
        logger = logging.getLogger(name)
        logger.debug(f"{name}: The file {event.dest_path} was created!")
        msg = NewFileFoundMsg(sender=name, path=event.dest_path)
        socket.send_string(json.dumps(msg.to_dict()))

    new_file_handler = PatternMatchingEventHandler(patterns=[frame_name_pattern])
    new_file_handler.on_moved = on_moved_event_handler

    new_file_observer = Observer()
    new_file_observer.schedule(
        event_handler=new_file_handler, path=working_dir, recursive=False
    )
    return new_file_observer


if __name__ == "__main__":
    log_directory.mkdir(exist_ok=True, parents=True)
    camera_frames_dir = Path(cam0_file_stream_path)
    camera_frames_dir.mkdir(exist_ok=True, parents=True)
    current_dir_observer = watch_and_notify(working_dir=camera_frames_dir, name="CAM0")
    current_dir_observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        current_dir_observer.stop()
        current_dir_observer.join()
