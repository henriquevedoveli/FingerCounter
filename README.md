# Gesture Tracker


## Description
_**Gesture Tracker**_ is a Python project that uses computer vision techniques to track and recognize hand gestures in real-time webcam feed. It leverages the power of the MediaPipe library for hand tracking and utilizes OpenCV for visualization and interaction. This project provides an interactive experience for detecting raised fingers and recognizing different hand positions, making it suitable for applications like gesture-controlled interfaces and interactive experiences.

## Directory Structure
```
GestureTracker/
    .gitignore
    .pre-commit-config.yaml
    Dockerfile
    requirements.txt
    run.sh
    src/
        handTracking.py
        main.py
```
- **.gitignore**: Specifies files and directories to be ignored by version control.
- **.pre-commit-config.yaml**:Configuration file for pre-commit hooks.
- **Dockerfile**: Docker configuration file to build the project environment.
- **requirements.txt**: A list of Python packages required for the project.
- **run.sh**: Bash script to run the Docker container with necessary configurations.
- **src/**: Directory containing the source code of the application.
  - **handTracking.py**: Python module containing the Detector class for hand tracking and gesture recognition.
  - **main.py**: Main application for real-time hand gesture tracking and visualization using OpenCV and MediaPipe.
 
## Features
- Real-time hand tracking and gesture recognition using a webcam feed.
- Utilizes the mediapipe library for accurate hand landmark detection.
- Recognizes a variety of hand gestures based on finger configurations.
- Provides a user-friendly interface for visualizing detected hand landmarks and gesture results.
- Dockerized environment for easy setup and execution.

## Instructions for Use:
1. Clone the repository and navigate to the project directory.
2. Build the Docker image using the provided Dockerfile:
```docker build -t gesture_tracker .```
3. Run the Docker container, passing the image name and any necessary environment settings:
```bash run.sh gesture_tracker```
This script (run.sh) simplifies the container execution process.

**Note**: Before running the project, ensure that Docker is installed on your system, and you have granted necessary permissions for webcam access. Additionally, you might need to adjust environment settings or install required dependencies within the Docker container to ensure proper functionality.

Feel free to customize the project, add new gestures, or integrate it into larger applications. GestureTracker provides a solid foundation for exploring the exciting world of gesture-based interfaces.

