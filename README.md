# Hand Gesture Recognition using Python and OpenCV

This project demonstrates real-time hand gesture recognition using Python and OpenCV. The application uses computer vision techniques to track and analyze hand landmarks in live video streams from a webcam. The goal is to recognize specific hand gestures, such as "thumbs up," "thumbs down," and the popular "rock-paper-scissors" signs.

## Requirements

To run the project, you need the following software installed on your system:

Python 3.x
* OpenCV
* cvzone library
You can install the required libraries using the following command:

Copy code
```
pip install opencv-python
pip install cvzone
pip install --upgrade numpy tensorflow
```

## How to Use
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the script hand_gesture_recognition.py using the following command:
## Copy code
```
python HandLandmarksDetection.py
```
1. A window will open displaying the webcam feed. Place your hand in front of the webcam and perform gestures like "thumbs up," "thumbs down," and "rock-paper-scissors."
2. The application will recognize the gestures and display the corresponding text on the screen.
### Supported Gestures
The application currently supports the following hand gestures:

1. Thumbs Up: Recognizes the gesture for a thumbs-up sign.
2. Thumbs Down: Recognizes the gesture for a thumbs-down sign.
3. Rock-Paper-Scissors: Recognizes the gesture for the popular game "rock-paper-scissors."
   
## Acknowledgments
The hand tracking functionality is implemented using the cvzone library, which simplifies hand detection and landmark tracking.

### Note
This project provides a basic implementation of hand gesture recognition using computer vision techniques. It may not be suitable for real-world applications that require complex sign language recognition. For more advanced sign language recognition, additional machine learning models and datasets are needed.

Feel free to use and modify the code for your own projects.
