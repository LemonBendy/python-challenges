#imports
import mediapipe as mp
import cv2

# --------------------
# Face Mesh Setup

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

#web cam setup
cap = cv2.VideoCapture(0)


with mp_face_mesh.FaceMesh(
    max_num_faces = 2,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5 ) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Empty camera frame, ignoring process")#if the camera is not working 
            continue
        image.flags.writeable = False # Make the image read only
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert the BGR image to RGB before processing.
        results = face_mesh.process(image) # Process the image
        image.flags.writeable = True # Make the image read only
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # C
        if results.multi_face_landmarks: # If the results are not empty
            for face_landmarks in results.multi_face_landmarks: # For each face
                #border around face, eyes and mouth
                mp_drawing.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image = image,
                    landmark_list = face_landmarks,
                    connections = mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())
        image = cv2.flip(image, 1) # Flip the image horizontally for a selfie-view display
        monitor_height = 650
        new_width = int(image.shape[1] * monitor_height / image.shape[0])
        image = cv2.resize(image, (new_width, monitor_height))
        cv2.imshow('Face Mesh', image)
        if cv2.waitKey(5) & 0xFF == 27: # If the user presses the escape key break the loop
            break
cap.release()
