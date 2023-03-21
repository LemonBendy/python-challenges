import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageFilter

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

bg_color = (192, 192, 192)
cap = cv2.VideoCapture(0)
with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
    bg_image = 'Project A-Level\\new_York.jpg'
    while cap.isOpened():
        success, image = cap.read()
        # image = #image.filter(ImageFilter.GaussianBlur(radius=20))
        if not success:
            print("Empty camera frame, ignoring process")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = selfie_segmentation.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        if bg_image is None:
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = bg_color
        output_image = np.where(condition, image, bg_image)
        cv2.imshow('MediaPipe Selfie Segmentation', output_image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()