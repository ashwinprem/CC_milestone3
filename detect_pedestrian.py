from ultralytics import YOLO
import cv2
import os

# Define image folder path
image_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/"
output_folder = "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/"
os.makedirs(output_folder, exist_ok=True)

# Load pre-trained YOLO model
model = YOLO("yolov8n.pt")  # Use "yolov8s.pt" for better accuracy

# List images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

for image_name in image_files:
    image_path = os.path.join(image_folder, image_name)
    image = cv2.imread(image_path)

    # Perform object detection
    results = model(image)

    # Extract pedestrian detections
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls.item())
            if class_id == 0:  # Pedestrian
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
                confidence = box.conf.item()

                # Draw bounding box
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f"Person: {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the detected pedestrian image
    output_path = os.path.join(output_folder, f"detected_{image_name}")
    cv2.imwrite(output_path, image)
    print(f"Saved detection result: {output_path}")

