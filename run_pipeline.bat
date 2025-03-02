@echo off
echo Starting Pedestrian Detection...
python detect_pedestrian.py
if %errorlevel% neq 0 (
    echo ERROR: Pedestrian detection failed!
    exit /b %errorlevel%
)
echo Pedestrian Detection Completed!

echo Starting Depth Estimation...
python depth_estimation.py
if %errorlevel% neq 0 (
    echo ERROR: Depth estimation failed!
    exit /b %errorlevel%
)
echo Depth Estimation Completed!

echo Starting Final Processing (Bounding Box + Depth Overlay)...
python final_processing.py
if %errorlevel% neq 0 (
    echo ERROR: Final Processing failed!
    exit /b %errorlevel%
)
echo Final Processing Completed!

echo ==================================
echo 🚀 Pipeline Execution Successful!
echo Processed files are in:
echo G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/
echo ==================================
pause

start explorer "G:/SOFE4630U-Design/Dataset_Occluded_Pedestrian/output/"

