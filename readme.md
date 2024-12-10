# Piano Motion by Doa Ibu

This is a motion-based piano application using **MediaPipe** for hand tracking and **Pygame** for sound. It detects finger positions from a webcam feed and plays corresponding musical notes based on finger gestures. The app uses **Streamlit** (now only locally can't deploy to cloud due to several reason) to display the live video feed and interact with the user.

## Features:
- **Hand Tracking**: Uses **MediaPipe** to detect and track hand landmarks.
- **Musical Notes**: Each finger represents a musical note, which plays when the finger is curled.
- **Web Interface**: Uses **Streamlit** to create an interactive web interface.
- **Sound**: Uses **Pygame** to play sounds associated with finger gestures.

---

## Requirements

Before running the app, make sure you have the following installed:

- **Python 3.x**
- **Streamlit**
- **OpenCV** (cv2)
- **MediaPipe**
- **Pygame**

To install the required libraries, you can use the following command:

```bash
pip install -r requirements.txt
```
Here’s what each dependency is used for:

- **streamlit**: For building the web interface.
- **opencv-python**: For webcam access and image processing.
- **mediapipe**: For hand tracking to detect finger gestures.
- **pygame**: For playing sound when a finger is curled.

---
## Usage

**1. Run the App:**
To start the application, run the following command:

```bash
streamlit run pianoMotionPrototype.py
```

**2. Interact with the App:**
Click on Start Video to begin the webcam stream.
Display Hand Landmarks: The system will detect your hand and display landmarks in real-time on the video feed.
Play Notes: The program will play a musical note when you curl a finger (thumb, index, middle, ring, or pinky).
Stop the Video: Click Stop Video to stop the webcam feed.

---
## How It Works

1. **Hand Tracking**: The app uses MediaPipe to track the user’s hand and detect finger landmarks (tip and MCP).

2. **Finger Gestures**: Each finger corresponds to a note:

  - Thumb: C
  - Index: D
  - Middle: E
  - Ring: F
  - Pinky: G
When the user curls a finger (i.e., forms a right angle between the finger tip and the MCP), the corresponding note is played.

3. **Sound**: The Pygame mixer is used to play a .wav sound file for each note when the corresponding finger is curled.

4. **User Interface**: The Streamlit app shows the live webcam feed, along with the hand landmarks and plays the sound for the correct note based on the finger gesture.

---
## Notes
- The app requires a webcam to capture the user's hand gestures.
- Make sure to grant permission for the app to access your webcam if prompted.
- You may need to tweak the finger gesture threshold or adjust the notes as per your preference.

---
## Troubleshooting
- **Webcam not working**: Ensure that your webcam is properly connected. On some platforms (e.g., Streamlit Cloud), webcam access may not be supported.
- **No sound**: Check if your audio device is connected and working. You can also try adjusting the pygame.mixer volume.

---
## Acknowledgements
- **MediaPipe**: For the hand tracking solution.
- **Pygame**: For audio playback functionality.
- **OpenCV**: For webcam handling and video feed processing.

