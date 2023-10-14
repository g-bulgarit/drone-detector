from ultralytics.engine.results import Results


def is_drone(model_res: Results, config: dict) -> bool:
    """
    Check if a drone is detected in the model results.

    This function iterates through the bounding boxes in the model results and
    checks if any of them correspond to a monitored class and meet a minimum
    detection confidence threshold.

    :param model_res: Results object containing bounding boxes
                      and their associated data.
    :type model_res: Results

    :param config: Configuration dictionary with parameters for detection.
                   It should include 'monitored_classes_ids' for monitored class IDs
                   and 'detection_confidence_threshold' for the confidence threshold.
    :type config: dict

    :return: True if a drone is detected based on the specified criteria,
             False otherwise.
    :rtype: bool
    """
    for box in model_res.boxes:
        if box.cls in config["monitored_classes_ids"]:
            if box.conf > config["detection_confidence_threshold"]:
                print("Drone Detected!")
                return True
    return False
