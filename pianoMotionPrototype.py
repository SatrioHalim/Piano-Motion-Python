import pygame
import cv2
import mediapipe as mp
import math
import streamlit as st
from threading import Thread

# Initialize Pygame
pygame.mixer.init()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Define finger landmarks
finger_landmarks = {
    "thumb": (mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.THUMB_MCP),
    "index": (mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.INDEX_FINGER_MCP),
    "middle": (mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_MCP),
    "ring": (mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_MCP),
    "pinky": (mp_hands.HandLandmark.PINKY_TIP, mp_hands.HandLandmark.PINKY_MCP),
}

# Define finger notes
finger_notes = {
    "thumb": "notes/C.wav",
    "index": "notes/D.wav",
    "middle": "notes/E.wav",
    "ring": "notes/F.wav",
    "pinky": "notes/G.wav",
}

# Mapping finger names to note texts
finger_text = {
    "thumb": "C",
    "index": "D",
    "middle": "E",
    "ring": "F",
    "pinky": "G",
}

active_notes = set()

# Function to calculate the distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def is_finger_closed(landmarks, tip, mcp, threshold=0.3):
    tip_to_mcp_distance = calculate_distance(landmarks[tip], landmarks[mcp])
    hand_scale = calculate_distance(landmarks[mp_hands.HandLandmark.WRIST], landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP])
    return tip_to_mcp_distance < hand_scale * threshold

def play_note_async(note):
    def play():
        pygame.mixer.Sound(note).play()
    Thread(target=play).start()

# Streamlit app
st.title("Piano Motion By Doa Ibu")
st.write("Dibuat oleh : ")
st.write("- Ida Bagus Davin Pidada (2702295556)")
st.write("- Satrio Halim Abdurrahman (2702298545)")
st.write("- Stephen Christian Augustien (2702281241)")
st.write("")

st.header("Petunjuk Penggunaan")
st.write("1. Pencet tombol start video untuk memulai program, tunggu sampai video muncul")
st.write("2. Gunakan satu telapak tangan untuk memainkan nada")
st.write("3. Tunjukan telapak tangan ke depan kamera sampai komputer dapat membaca struktur telapak tangan")
st.write("(Diwakili oleh garis-garis dan titik merah pada layar)")
st.write("4. Untuk memainkan salah satu nada, tekuk jari hingga membentuk sudut siku-siku")
st.write("")

st.subheader("Selamat Mencoba !")
st.write("")

# State management for start and stop
if "capture_running" not in st.session_state:
    st.session_state.capture_running = False

start_button = st.button("Start Video", key="start_button")
stop_button = st.button("Stop Video", key="stop_button")

if start_button:
    st.session_state.capture_running = True

if stop_button:
    st.session_state.capture_running = False

# Initialize video capture
cap = None
if st.session_state.capture_running:
    cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()

# Main loop for video feed
while st.session_state.capture_running:
    ret, frame = cap.read()
    if not ret:
        st.error("Cannot access webcam.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_notes = []  # Reset the list of notes for this frame

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for finger, (tip, mcp) in finger_landmarks.items():
                if is_finger_closed(hand_landmarks.landmark, tip, mcp):
                    if finger not in active_notes:
                        active_notes.add(finger)
                        play_note_async(finger_notes[finger])
                    # Add the note text to the current notes list
                    current_notes.append(finger_text[finger])
                else:
                    active_notes.discard(finger)

    # Display the current notes in the top-left corner
    if current_notes:
        notes_text = " ".join(current_notes)
        cv2.putText(frame, notes_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame_placeholder.image(frame, channels="BGR")

if cap:
    cap.release()
pygame.quit()
