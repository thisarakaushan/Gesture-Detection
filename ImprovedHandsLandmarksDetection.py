import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as auto

# Initialize the HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)  # Detecting multiple hands

# Gesture recognition logic
def recognize_gesture(lmList):
    if len(lmList) == 21:
        # Thumbs Up Gesture
        if lmList[4][1] < lmList[17][1]:  # Check if the thumb is below the index finger
            return "thumbs up"
        
        # Thumbs Down Gesture
        if lmList[4][1] > lmList[17][1]:  # Check if the thumb is above the index finger
            return "thumbs down"
        
        # Rock-Paper-Scissors Gesture
        # Customize this part based on your own landmark positions for the rock-paper-scissors gesture
        # For simplicity, we will just check the position of the middle finger
        if lmList[12][2] < lmList[6][2]:  # Check if the middle finger is lower than the ring finger
            return "rock"
        elif lmList[12][2] > lmList[6][2]:  # Check if the middle finger is higher than the ring finger
            return "paper"
        else:
            return "scissors"
    return None

while True:
    # Get image frame
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        for hand in hands:
            # Hand Landmarks
            HandLandMarkList = hand["lmList"]
            
            # Gesture Recognition
            gesture = recognize_gesture(HandLandMarkList)
            if gesture:
                print("Detected Gesture:", gesture)
                # Perform actions based on the recognized gesture, e.g., print or speak the gesture
                
                # Perform different actions based on the recognized gesture
                if gesture == "thumbs up":
                    # Do something for thumbs up gesture
                    auto.press('up')
                elif gesture == "thumbs down":
                    # Do something for thumbs down gesture
                    auto.press('down')
                elif gesture == "rock":
                    # Do something for rock gesture
                    auto.write("rock")
                elif gesture == "paper":
                    # Do something for paper gesture
                    auto.write("paper")
                elif gesture == "scissors":
                    # Do something for scissors gesture
                    auto.write("scissors")

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break