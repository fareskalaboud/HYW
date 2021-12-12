import cv2
import mediapipe as mp
import os
import sys
import importlib
from poses_comparison import compare_poses
from glob import glob
import json

sys.path.append('./openpose_2/openpose/build/examples/tutorial_api_python')
# Considering your module contains a function called my_func, you could import it:
# from 01_body_from_image import *

# puzzle = __import__('01_body_from_image')
puzzle = __import__('04_keypoints_from_images')

# importlib.import_module(01_body_from_image.py, package=None)
# npose/build/examples/tutorial_api_python/01_body_from_image import *
global camera
camera = cv2.VideoCapture(0)

# pose_parts = ["nose", "L_eye_IN", "L_eye", "L_eye_OUT", "R_eye_IN", "R_eye", "R_eye_OUT", "L_ear", "R_ear", "L_mouth", "R_mouth", "L_shoulder", "R_shoulder", "L_elbow", "R_elbow",
#               "L_wrist", "R_wrist", "L_pinky", "R_pinky", "L_index", "R_index", "L_thumb", "R_thumb", "L_hip", "R_hip", "L_knee", "R_knee", "L_ankle", "R_ankle", "L_heel", "R_heel", "L_foot", "R_foot"]

# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()


body_parts = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee",\
 "RAnkle", "LHip", "LKnee", "LAnkle", "REye", 'LEye', "REar", "LEar", "LBigToe", "LSmallToe", "LHeel",\
  "RBigToe", "RSmallToe", "RHeel", "Background"]


print(len(body_parts))
global json_files
json_files = glob('PoseVideos/output/vid2vid/test_openpose'+'/*.json')

# f = open (json_files[0], "r")
# data = json.loads(f.read())
# print(data['people'][0]['pose_keypoints_2d'])

def gen_frames():
    poseKeypoints = []
    c = 0
    iou_all_frames = []
    while True:
        try:
            success, img = camera.read()  # read the camera frame


            #####################################
            try:
                poseKeypoints = puzzle.parseStresamImage(img)
    
                iou_per_frame, song_keypoints = compare_poses(poseKeypoints[0],json_files, c)
                if iou_per_frame > 0.1: print(iou_per_frame)
                iou_all_frames.append(iou_per_frame)
                c += 1
            except:
                c = c

            if not success:
                break
            else:
                try:
                    # cv2.putText(img, 'hi', (500,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
                    
                    # src = cv2.imread('PoseVideos/output/vid2vid/test_img/output_0001.jpg')
                    # tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
                    # _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
                    # b, g, r = cv2.split(src)
                    # rgba = [b,g,r, alpha]
                    # dst = cv2.merge(rgba,4)
                    # cv2.imwrite("PoseVideos/output/vid2vid/output_0001.png", dst)
                    # dst = cv2.imread("PoseVideos/output/vid2vid/output_0001.png")
                    
                    # dst = cv2.resize(dst, (300,300), interpolation = cv2.INTER_AREA)



                    # b,g,r,a = cv2.split(src)
                    # dst = cv2.merge((b,g,r))

                    # mask = cv2.medianBlur(a,5)

                    # # Black-out the area behind the logo in our original ROI
                    # img1_bg = cv2.bitwise_and(img.copy(),img.copy(),mask = cv2.bitwise_not(mask))

                    # # Mask out the logo from the logo image.
                    # img2_fg = cv2.bitwise_and(dst,dst,mask = mask)

                    # # Update the original image with our new ROI
                    # img = cv2.add(img1_bg, img2_fg)




                    # y_offset = 200
                    # x_offset = 200

                    # img[y_offset:y_offset+dst.shape[0], x_offset:x_offset+dst.shape[1]] = dst

                    # y1, y2 = y_offset, y_offset + dst.shape[0]
                    # x1, x2 = x_offset, x_offset + dst.shape[1]

                    # _,alpha_s = cv2.threshold(dst,0,255,cv2.THRESH_BINARY)
                    # # alpha_s = dst[:, :, 3] / 255.0
                    # alpha_l = 1.0 - alpha_s

                    # print(alpha_s)

                    # for c in range(0, 3):
                    #     img[y1:y2, x1:x2, c] = (alpha_s * dst[:, :, c] +
                    #                             alpha_l * img[y1:y2, x1:x2, c])


                    # img = cv2.circle(img, (int(song_keypoints[0]), int(song_keypoints[1])), radius=7, color=(0, 0, 255), thickness=-1)
                    # img = cv2.circle(img, (int(song_keypoints[2]), 500), radius=7, color=(0, 0, 255), thickness=-1)


                    ret, buffer = cv2.imencode('.jpg', img[0:720,260:980])
                    img = buffer.tobytes()
                
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result
                except:
                    print('caught the error')

        except:
            camera.release()

    return iou_all_frames