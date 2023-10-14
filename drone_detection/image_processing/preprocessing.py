import cv2
from pathlib import Path


def preprocess_frame(frame_path: Path, output_dir: Path) -> None:
    """
    Check if a drone is detected in the model results.

    This function iterates through the bounding boxes in the model results and
    checks if any of them correspond to a monitored class and meet a minimum
    detection confidence threshold.

    :param model_res: Results object containing bounding boxes and their associated data.
    :type model_res: Results

    :param config: Configuration dictionary with parameters for detection.
                   It should include 'monitored_classes_ids' for monitored class IDs
                   and 'detection_confidence_threshold' for the confidence threshold.
    :type config: dict

    :return: True if a drone is detected based on the specified criteria, False otherwise.
    :rtype: bool
    """
    image_frame_count = Path(frame_path).stem
    image = cv2.imread(str(frame_path))
    h, w, _ = image.shape
    tilex = w // 2
    tiley = h // 2
    tile_counter = 0
    for y in range(0, h, tiley):
        for x in range(0, w, tilex):
            output_filename = f"{output_dir}/{image_frame_count}_{tile_counter}.jpg"
            tile = image[y: y + tiley, x: x + tilex]
            cv2.imwrite(filename=output_filename, img=tile)
            tile_counter += 1
