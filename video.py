# import streamlit as st

# def main():
#     st.title("Streamlit Video Player")

#     #Google Drive video URL VIDEO .mp4
#     video_url = "https://firebasestorage.googleapis.com/v0/b/fir-ec695.appspot.com/o/t-15%2Finput_side.mp4?alt=media&token=0cf29a63-b98b-451a-a9f5-7e2d71caf9c3"  # Replace "your-file-id" with the actual file ID
#     #video_url = "https://drive.google.com/file/d/1gurNIOzlaJ76GsWHXcSz8Ua-bKYkllcw/view?usp=drive_link"
#     #Display the video
#     st.video(video_url)


# if __name__ == "__main__":
#     main()

import streamlit as st
import cv2

def main():
    st.title("Streamlit Webcam Player")

    cap = cv2.VideoCapture(0)
    load = st.button("STOP")
    stframe = st.empty()

    left_limits1 = [0, 450, 1920,450]
    left_limits2 = [0, 500, 1920,500]
    
    while not load:
        success, img = cap.read()
        cv2.line(img, (left_limits1[0], left_limits1[1]), (left_limits1[2], left_limits1[3]), (0, 0, 255), 5)
        cv2.line(img, (left_limits2[0], left_limits2[1]), (left_limits2[2], left_limits2[3]), (255, 0, 0), 5)

        
        if not success:
            break

        # Display the frame in the video element
        stframe.image(img, channels='BGR', use_column_width=True)

if __name__ == "__main__":
    main()
