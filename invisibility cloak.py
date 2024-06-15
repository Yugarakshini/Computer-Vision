# Importation
import cv2 
import numpy as np
import time

fourCC = cv2.VideoWriter_fourcc(*'XVID')
# this is used to capture video in OpenCV
# fourCC is a 4-byte video code, used to specify the video code
# for Windows, the video code is "*'XVID'" and for Mac, it is "*'MJPG'"

out = cv2.VideoWriter('output.avi', fourCC, 20, (200, 200))
# (fileName, fourCCvariable, framesPerSec, frameSize)

cap = cv2.VideoCapture(0)  # you can use 0 or 1 to capture the video

time.sleep(3) 
# 3 second delay to give time for the settings to process before webcam starts

# variables
count = 0
background = 0 

# while this forloop runs, capture the background 
for i in range(60): # capturing the bkgrd 60 times, and overlapping to make one
    returnV, background = cap.read() 
    # returnV is a boolean value which returns True if captured properly
    # background is the captured background in an array of pixels 
    
background = np.flip(background, axis=1) 
# flipping the background to avoid mirror image

while(cap.isOpened()): # while your camera is opened, this will run
    returnV, img = cap.read() # returnV is true or false
    if not(returnV): # if at any point, return becomes false, break the loop
        break
    count += 1 # keeping count of the number of times this run (no use1)
    img = np.flip(img, axis=1) # flipping the current video 
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # converting your image to HSV
    lower_red = np.array([0, 120, 50]) # saturation is 120-255, value is 50-255
    upper_red = np.array([10, 255, 255]) # https://tinyurl.com/hsvColors
    mask1 = cv2.inRange(hsv, lower_red, upper_red) 
    # detecting wheter image pixel colors are in range of the colors
    # creates binary mask, so binary operations can be used 
