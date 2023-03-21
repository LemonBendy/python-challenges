import os
import cv2
import numpy
import argparse
import streamlit as st
from PIL import Image, ImageEnhance

from face_detection import select_face, select_all_faces
from face_swap import face_swap

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FaceSwapApp')
    parser.add_argument('--correct_color', default=True, action='store_true', help='Correct color')
    parser.add_argument('--warp_2d', default=False, action='store_true', help='2d or 3d warp')
    args = parser.parse_args()

    uploaded_source_file = st.file_uploader("Source File", type=['jpg', 'png', 'jpeg'])
    uploaded_target_file = st.file_uploader("Target File", type=['jpg', 'png', 'jpeg'])

    if uploaded_source_file is not None and uploaded_target_file is not None:
        source_image = Image.open(uploaded_source_file)
        target_image = Image.open(uploaded_target_file)

        # Convert images from PIL to CV2
        src_img = cv2.cvtColor(numpy.array(source_image), cv2.IMREAD_COLOR)
        dst_img = cv2.cvtColor(numpy.array(target_image), cv2.IMREAD_COLOR)

        # Select src face
        src_points, src_shape, src_face = select_face(src_img)
        # Select dst face
        dst_faceBoxes = select_all_faces(dst_img)

        if dst_faceBoxes is None:
            print('Detect 0 Face !!!')
            exit(-1)

        output = dst_img
        for k, dst_face in dst_faceBoxes.items():
            output = face_swap(src_face, dst_face["face"], src_points,
                               dst_face["points"], dst_face["shape"],
                               output, args)

            st.markdown('<p style="text-align: left;">Result</p>', unsafe_allow_html=True)
            st.image(output, width=500)