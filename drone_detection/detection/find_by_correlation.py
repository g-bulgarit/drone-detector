import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.figure import Figure

from drone_detection.detection.detection_types import BoundingBox


def find_anomalies(image_path: str, kernel_size: int, k: int) -> list[BoundingBox]:
    bounding_boxes: list[BoundingBox] = []
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the mean color value of the input image
    mean_color = np.mean(image, axis=(0, 1))
    kernel = mean_color

    # Perform the cross-correlation using OpenCV's filter2D function
    # and flatten the correlation result
    correlation_result = cv2.filter2D(image, -1, kernel)
    flattened_corr = correlation_result.flatten()

    # Get the indices that would sort the correlation values (ascending order)
    smallest_indices = np.argpartition(flattened_corr, k)[:k]
    largest_indices = np.argpartition(flattened_corr, -k)[-k:]

    # Get the coordinates of the K smallest and K largest correlations
    smallest_locations = np.unravel_index(smallest_indices, correlation_result.shape)
    largest_locations = np.unravel_index(largest_indices, correlation_result.shape)

    # Draw red rectangles around the K smallest and K largest kernels
    for i in range(k):
        bounding_boxes.append(
            BoundingBox(
                ymax=largest_locations[0][i] - kernel_size // 2,
                ymin=smallest_locations[0][i] - kernel_size // 2,
                xmin=smallest_locations[1][i] - kernel_size // 2,
                xmax=largest_locations[1][i] - kernel_size // 2,
                kernel_size=kernel_size,
            )
        )

    return bounding_boxes


def draw_anomalies_on_image(
    image_path: str, bounding_boxes: list[BoundingBox]
) -> Figure:
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()

    ax.imshow(image)
    ax.axis("off")

    for box in bounding_boxes:
        rect_min = patches.Rectangle(
            (box.xmin, box.ymin),
            box.kernel_size,
            box.kernel_size,
            linewidth=2,
            edgecolor="r",
            facecolor="none",
        )
        rect_max = patches.Rectangle(
            (box.xmax, box.ymax),
            box.kernel_size,
            box.kernel_size,
            linewidth=2,
            edgecolor="b",
            facecolor="none",
        )

        ax.add_patch(rect_min)
        ax.add_patch(rect_max)

    return fig


if __name__ == "__main__":
    # Replace with the actual path to your JPEG image
    image_path = "D:\Code\drone-detection\sky-001a.jpg"
    kernel_size = 10  # Adjust the kernel size as needed
    k = 3  # Specify the number of K smallest and K largest correlations

    anomalies = find_anomalies(image_path, kernel_size, k)
    fig = draw_anomalies_on_image(image_path, anomalies)
    fig.show()
