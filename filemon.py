import sys
import zmq
from packages.configuration.config import frame_name_pattern, ZMQ_NEW_FILE_PUB_PORT
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileCreatedEvent
from packages.communication.messages import NewFileFoundMsg
import json


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://127.0.0.1:{ZMQ_NEW_FILE_PUB_PORT}")

file_handler = logging.FileHandler(filename="filemon.log")
stdout_handler = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[file_handler, stdout_handler],
)


def on_created_event_handler(event: FileCreatedEvent) -> None:
    logger = logging.getLogger()
    logger.debug(f"The file {event.src_path} was created!")
    msg = NewFileFoundMsg(sender="tbd", path=event.src_path)
    socket.send_string(json.dumps(msg.to_dict()))


def watch_and_notify(working_dir: Path) -> Observer:
    logger = logging.getLogger()
    logger.debug(f"Started logging new files at {working_dir}")
    new_file_handler = PatternMatchingEventHandler(patterns=[frame_name_pattern])
    new_file_handler.on_created = on_created_event_handler

    new_file_observer = Observer()
    new_file_observer.schedule(
        event_handler=new_file_handler, path=working_dir, recursive=False
    )
    return new_file_observer


if __name__ == "__main__":
    my_dir = Path(r"D:\Code\drone-detection")
    current_dir_observer = watch_and_notify(working_dir=my_dir)
    current_dir_observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        current_dir_observer.stop()
        current_dir_observer.join()
