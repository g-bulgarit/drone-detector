import numpy as np
import numpy.typing as npt
import time
import cv2
from pathlib import Path


def generate_random_image(width: int, height: int) -> npt.NDArray[np.uint8]:
    image = np.random.rand(width, height) * 255
    return image.astype(np.uint8)


def generate_random_jpg(save_dir: Path, filename: str, shape: tuple) -> None:
    image = generate_random_image(*shape)
    output_filename = str(save_dir / filename)
    cv2.imwrite(filename=output_filename, img=image)


if __name__ == "__main__":
    framerate = 10  # frames / sec
    frame_counter = 0
    save_dir = Path(r"D:\Code\drone-detection\frames")
    resolution = (480, 640)
    while True:
        generate_random_jpg(save_dir, f"{frame_counter}.jpg", resolution)
        time.sleep(1 / framerate)
        frame_counter += 1
