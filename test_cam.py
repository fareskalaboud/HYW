import cv2
import mediapipe as mp
import os
import sys
import importlib


camera = cv2.VideoCapture(0)
success, img = camera.read()
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)