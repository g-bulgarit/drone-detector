from pathlib import Path
import shlex
import subprocess

from drone_detection.configuration.config import (
    CAM0_FILE_STREAM_PATH,
    RESOLUTION,
    FPS,
)


if __name__ == "__main__":
    output_dir = Path(CAM0_FILE_STREAM_PATH)
    output_dir.mkdir(exist_ok=True, parents=True)
    camera_name = "cam0"
    camera_device = "/dev/video0"

    launch_cmd = f"""
    gst-launch-1.0 v4l2src device={camera_device} \
    ! "image/jpeg,width={RESOLUTION[0]},height={RESOLUTION[1]},framerate={FPS}/1" \
    ! videorate \
    ! "image/jpeg,framerat={FPS}/1" \
    ! multifilesink location='{CAM0_FILE_STREAM_PATH}/{camera_name}_%06d.jpg'
    """
    subprocess.Popen(shlex.split(launch_cmd))
