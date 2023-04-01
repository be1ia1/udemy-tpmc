import streamlit as st
import cv2
from datetime import datetime


st.title('Motion Detector')
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        now = datetime.now()
        first_line = now.strftime('%A')
        cv2.putText(img=frame, text=first_line, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        second_line = now.strftime("%H:%M:%S")
        cv2.putText(img=frame, text=second_line, org=(50, 90),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)