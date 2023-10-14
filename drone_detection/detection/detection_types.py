from dataclasses import dataclass


@dataclass
class BoundingBox:
    ymin: int
    ymax: int
    xmin: int
    xmax: int
    kernel_size: int
