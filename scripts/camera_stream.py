from pathlib import Path
import shlex
import subprocess

from drone_detection.configuration.config import cam0_file_stream_path

if __name__ == "__main__":
    output_dir = Path(cam0_file_stream_path)
    output_dir.mkdir(exist_ok=True, parents=True)
    camera_name = "cam0"
    camera_device = "/dev/video0"

    launch_cmd = f"""
    gst-launch-1.0 v4l2src device={camera_device} \
    ! "image/jpeg,width=2592,height=1944,framerate=1/1" \
    ! videorate \
    ! "image/jpeg,framerate=1/1" \
    ! multifilesink location='{cam0_file_stream_path}/{camera_name}_%06d.jpg'
    """

    subprocess.Popen(shlex.split(launch_cmd))
