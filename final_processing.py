import cv2
import numpy as np
import os

# Define image folder path
image_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/"
depth_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/"
output_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/"

os.makedirs(output_folder, exist_ok=True)

# List images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

for image_name in image_files:
    # Load detected pedestrian image
    detected_image_path = os.path.join(depth_folder, f"detected_{image_name}")
    depth_image_path = os.path.join(depth_folder, f"depth_{image_name}")

    if not os.path.exists(detected_image_path) or not os.path.exists(depth_image_path):
        print(f"Skipping {image_name}, missing depth or detection results")
        continue

    detected_image = cv2.imread(detected_image_path)
    depth_map = cv2.imread(depth_image_path, cv2.IMREAD_GRAYSCALE)

    # Extract the bounding box and estimate depth
    for y in range(depth_map.shape[0]):
        for x in range(depth_map.shape[1]):
            if detected_image[y, x, 1] == 255:  # Checking green channel
                avg_depth = np.mean(depth_map[max(0, y - 5): y + 5, max(0, x - 5): x + 5])

                # Draw depth estimation on the image
                cv2.putText(detected_image, f"Depth: {avg_depth:.2f}m", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Save final image
    output_path = os.path.join(output_folder, f"final_{image_name}")
    cv2.imwrite(output_path, detected_image)
    print(f"Saved final image with depth: {output_path}")

