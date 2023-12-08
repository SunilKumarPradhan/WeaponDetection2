import os
import streamlit as st
import cv2
import imutils
from helpers import weapon_detector  # Assuming you have a weapon_detector function in helpers.py
import numpy as np

def app():
    st.write("# DeductAI: Weapon Detector")

    st.write("## Upload Video in .mp4 format")
    uploaded_video = st.file_uploader("", type=["mp4"])

    st.write("## Uploaded Video")

    if uploaded_video:
        st.video(uploaded_video)

        button = st.button("Detect Weapons", key=None)

        if button:
            # Initialize video capture
            video_path = "uploaded_video.mp4"
            with open(video_path, "wb") as video_file:
                video_file.write(uploaded_video.read())

            # Initialize video capture
            camera = cv2.VideoCapture(video_path)

            # Initialize variables
            weapon_exist = False

            while True:
                (grabbed, frame) = camera.read()

                # if the frame could not be grabbed, then we have reached the end of the video
                if not grabbed:
                    break

                # Resize the frame, convert it to grayscale, and blur it
                frame = imutils.resize(frame, width=500)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)

                # Detect weapons in the frame
                weapon_detected = weapon_detector.detect(frame)  # Assuming you have a detect function in helpers.py

                if weapon_detected:
                    weapon_exist = True

                # Display the frame
                st.image(frame, channels="BGR")

                # if the user presses the stop button
                if not st.button("Stop Detection"):
                    break

            if weapon_exist:
                st.markdown("### Weapons detected! 🔫")
            else:
                st.markdown("### Weapons NOT detected!")

            # Cleanup
            camera.release()
            os.remove(video_path)
