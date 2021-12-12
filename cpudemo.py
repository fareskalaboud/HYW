import cv2
import mediapipe as mp
import time

pose_parts = ["nose", "L_eye_IN", "L_eye", "L_eye_OUT", "R_eye_IN", "R_eye", "R_eye_OUT", "L_ear", "R_ear", "L_mouth", "R_mouth", "L_shoulder", "R_shoulder", "L_elbow", "R_elbow", "L_wrist", "R_wrist", "L_pinky", "R_pinky", "L_index", "R_index", "L_thumb", "R_thumb", "L_hip", "R_hip", "L_knee", "R_knee", "L_ankle", "R_ankle", "L_heel", "R_heel", "L_foot", "R_foot"]

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(1)
pTime = 0

while True:
    printed = False

    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(pose_parts[id], lm)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)
    cv2.imshow('Image', img)

    cv2.waitKey(1)