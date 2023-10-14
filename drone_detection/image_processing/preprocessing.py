import cv2
from pathlib import Path


def preprocess_frame(frame_path: Path, output_dir: Path) -> None:
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
