import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as auto

# Initialize the HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)  # Detecting multiple hands

while True:
    # Get image frame
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        for hand in hands:
            # Hand Landmarks
            HandLandMarkList = hand["lmList"]
            
            # Hand Gesture Recognition
            # Example: Detecting thumbs up gesture
            if HandLandMarkList[4][1] < HandLandMarkList[17][1]:  # Check if the thumb is below the index finger
                auto.press('up')  # Perform an action when thumbs up gesture is detected
                
            # Additional Gesture Recognition can be added for other hand gestures

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break