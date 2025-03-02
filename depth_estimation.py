import torch
import cv2
import numpy as np
import os

# Load MiDaS depth estimation model
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.eval()

# Define image folder path
image_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/"
output_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/"
os.makedirs(output_folder, exist_ok=True)

# List images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

for image_name in image_files:
    image_path = os.path.join(image_folder, image_name)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    input_image = cv2.resize(image, (256, 256))

    # Convert to tensor
    input_tensor = torch.tensor(input_image).permute(2, 0, 1).unsqueeze(0).float()

    # Predict depth
    with torch.no_grad():
        depth_map = midas(input_tensor)

    # Convert depth map to numpy array
    depth_map = depth_map.squeeze().numpy()
    depth_map = (depth_map - np.min(depth_map)) / (np.max(depth_map) - np.min(depth_map)) * 255
    depth_map = depth_map.astype(np.uint8)

    # Save depth map
    output_path = os.path.join(output_folder, f"depth_{image_name}")
    cv2.imwrite(output_path, depth_map)
    print(f"Saved depth map: {output_path}")

