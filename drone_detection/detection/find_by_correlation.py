import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def load_run_and_plot(image_path, kernel_size, k):
    # Load the JPEG image from disk using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to load the image from {image_path}")
        return

    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the mean color value of the input image
    mean_color = np.mean(image, axis=(0, 1))

    # Create a kernel with the mean color value
    kernel = mean_color

    # Perform the cross-correlation using OpenCV's filter2D function
    correlation_result = cv2.filter2D(image, -1, kernel)

    # Flatten the correlation result
    flattened_corr = correlation_result.flatten()

    # Get the indices that would sort the correlation values (ascending order)
    smallest_indices = np.argpartition(flattened_corr, k)[:k]
    largest_indices = np.argpartition(flattened_corr, -k)[-k:]

    # Sort the correlation values
    smallest_correlations = flattened_corr[smallest_indices]
    largest_correlations = flattened_corr[largest_indices]

    # Get the coordinates of the K smallest and K largest correlations
    smallest_locations = np.unravel_index(
        smallest_indices, correlation_result.shape)
    largest_locations = np.unravel_index(
        largest_indices, correlation_result.shape)

    # Plot the image
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis('off')

    # Draw red rectangles around the K smallest and K largest kernels
    for i in range(k):
        y_min, x_min = smallest_locations[0][i] - \
            kernel_size // 2, smallest_locations[1][i] - kernel_size // 2
        y_max, x_max = largest_locations[0][i] - \
            kernel_size // 2, largest_locations[1][i] - kernel_size // 2

        # Draw rectangles around the K smallest kernels
        rect_min = patches.Rectangle(
            (x_min, y_min), kernel_size, kernel_size, linewidth=2, edgecolor='r', facecolor='none')
        rect_max = patches.Rectangle(
            (x_max, y_max), kernel_size, kernel_size, linewidth=2, edgecolor='r', facecolor='none')

        plt.gca().add_patch(rect_min)
        plt.gca().add_patch(rect_max)

    plt.show()


if __name__ == "__main__":
    # Replace with the actual path to your JPEG image
    image_path = "assets/sky-001a.jpg"
    kernel_size = 10  # Adjust the kernel size as needed
    k = 3  # Specify the number of K smallest and K largest correlations

    load_run_and_plot(image_path, kernel_size, k)
