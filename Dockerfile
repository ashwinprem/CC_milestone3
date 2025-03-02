# Use the official Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (for OpenCV, YOLO, and ML models)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    apache-beam[gcp] \
    google-cloud-storage \
    google-cloud-pubsub \
    ultralytics \
    opencv-python \
    numpy \
    torch \
    timm

# Copy all project files into the container
COPY . .

# Set the entrypoint command for the container
ENTRYPOINT ["python", "dataflow_pipeline.py"]

