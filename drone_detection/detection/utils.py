from ultralytics.engine.results import Results


def is_drone(model_res: Results, config: dict) -> bool:
    for box in model_res.boxes:
        if box.cls in config["monitored_classes_ids"]:
            if box.conf > config["detection_confidence_threshold"]:
                print("Drone Detected!")
                return True
    return False
