import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
import time
import copy

# set up SIFT and video
sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
video = cv2.VideoCapture(0)

counter = 0
while video.isOpened():
    counter += 1

    _, im1 = video.read() # (360, 640)
    im2 = copy.deepcopy(im1)
    # im2 = im2[90:270, 230:410]
    im2 = ndimage.rotate(im2, 30)[210:410, 270:510]
    # im2 = cv2.filter2D(ndimage.rotate(im2, 30)[210:410, 270:510], -1, np.ones((5, 5), np.float32)/25)

    start = time.time()

    im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    kp1, desc1 = sift.detectAndCompute(im1, None)
    kp2, desc2 = sift.detectAndCompute(im2, None)

    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)

    end = time.time()
    totalTime = end - start
    fps = 1 / totalTime
    if counter % 10 == 0:
        print("FPS: ", fps)

    im3 = cv2.drawMatches(im1, kp1, im2, kp2, matches[:50], im2, flags=2)
    cv2.imshow('SIFT', im3)
    if cv2.waitKey(5) & 0xFF == 27:
        break

video.release()