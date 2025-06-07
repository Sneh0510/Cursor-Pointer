#             Cursor-Wave
==============================================

A mini project using AI and ML to control the mouse cursor using hand gestures.

-------------------------------------------
PROJECT DESCRIPTION
-------------------------------------------

Cursor-Wave is a gesture-controlled mouse built with Python. It uses computer vision and machine learning to detect hand movements through a webcam and translates them into mouse movements and clicks.

With the help of MediaPipe, OpenCV, and PyAutoGUI, this application detects the position of your fingers in real time and allows you to:

- Move the cursor using your index finger
- Perform a left-click when your index finger and thumb touch
- Perform a right-click when your thumb and middle finger touch

-------------------------------------------
FEATURES
-------------------------------------------

✔ Real-time hand tracking with MediaPipe  
✔ Cursor movement mapped to finger tip  
✔ Left click via index and thumb touch  
✔ Right click via middle finger and thumb touch  
✔ Natural interaction using webcam  

-------------------------------------------
TECHNOLOGIES USED
-------------------------------------------

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

-------------------------------------------
SETUP & INSTALLATION
-------------------------------------------

1. Install Python 3.6 or above.
2. Clone or download the project folder.
   ```
   git clone https://github.com/Sneh0510/Cursor-Wave.git
   cd cursor-wave
   ```
4. Install the required libraries using pip:
   ```
   pip install opencv-python mediapipe pyautogui numpy
   ```
5. Run the script:
   ```
   python cursor_wave.py
   ```
6. Use your hand in front of the webcam to control the mouse.

   Press ESC to quit.

-------------------------------------------
FUTURE ENHANCEMENTS
-------------------------------------------

- Add gesture customization via GUI  
- Scroll functionality using finger gestures  
- Multi-hand gesture support  
- More stable gesture detection with fine-tuned thresholds  

-------------------------------------------
ACKNOWLEDGEMENTS
-------------------------------------------

- MediaPipe by Google
- OpenCV
- PyAutoGUI
- NumPy

-------------------------------------------
DEVELOPER
-------------------------------------------

Developed by Sneh Yadav  
GitHub: https://github.com/sneh0510
