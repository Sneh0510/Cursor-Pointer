import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize Mediapipe and pyautogui
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert BGR frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Drawing the landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger and thumb
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Normalize the coordinates
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # Map the coordinates to screen dimensions
            screen_x = np.interp(x, [0, frame_width], [0, screen_width])
            screen_y = np.interp(y, [0, frame_height], [0, screen_height])

            # Move the mouse pointer
            pyautogui.moveTo(screen_x, screen_y)

            # Calculate the distance between the index finger and thumb
            distance = np.linalg.norm(np.array([thumb_tip.x, thumb_tip.y]) - np.array([index_finger_tip.x, index_finger_tip.y]))
            distance_middle_finger = np.linalg.norm(np.array([hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, 
                                                              hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y]) - 
                                                     np.array([thumb_tip.x, thumb_tip.y]))

            # Left click gesture (index and thumb close)
            if distance < 0.05:
                pyautogui.click()
                print("Left Click detected")

            # Right click gesture (thumb and middle finger close)
            if distance_middle_finger < 0.05:
                pyautogui.rightClick()
                print("Right Click detected")

            # Optional: Display landmarks and gestures
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)  # Index finger tip
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), -1)  # Thumb tip

    # Show the frame with landmarks
    cv2.imshow("AI Gesture Mouse", frame)

    # Exit with ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()    
