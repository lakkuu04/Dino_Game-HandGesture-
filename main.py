import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey
import time

# Constants for the space key (for jumping)
SPACE_KEY = 0x39

# Initialize the HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Time delay to allow you to switch to the Dino game window
time.sleep(2.0)

# Set for currently pressed keys
current_key_pressed = set()

# Video capture from the webcam
video = cv2.VideoCapture(0)

# Function to handle the key press
def press_space_key():
    PressKey(SPACE_KEY)
    time.sleep(0.05)  # Adjust this value for smoother jumps
    ReleaseKey(SPACE_KEY)

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # Detect hands in the frame
    hands, img = detector.findHands(frame)
    
    # Draw rectangles on the frame
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    
    if hands:
        lmlist = hands[0]
        fingerUp = detector.fingersUp(lmlist)
        print(fingerUp)
        
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Jumping', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            if SPACE_KEY not in current_key_pressed:
                press_space_key()
                current_key_pressed.add(SPACE_KEY)
        else:
            if SPACE_KEY in current_key_pressed:
                current_key_pressed.remove(SPACE_KEY)
        
        if fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Finger Count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Finger Count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger Count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger Count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
