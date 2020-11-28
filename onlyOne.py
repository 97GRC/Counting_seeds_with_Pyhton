#!/usr/bin/env python3

import cv2                          # package to image manipulation
import numpy as np

#########
#FUNÇÃO
img = cv2.imread('avc.jpg') 

def seeds_number(img):
	blur = cv2.blur(img, (50, 50))
	grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	th = cv2.threshold(grey, 60, 255, cv2.THRESH_BINARY)[1]
	sp = cv2.morphologyEx(th,
                       cv2.MORPH_OPEN,
                       np.ones((10, 10), np.uint8),
                       iterations = 4)
	contours, hierarchy = cv2.findContours(th,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
	return len(contours)

print(seeds_number(img))



###########
img = cv2.imread('avc.jpg')

blur = cv2.blur(img, (50, 50))
grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
th = cv2.threshold(grey, 60, 255, cv2.THRESH_BINARY)[1]
sp = cv2.morphologyEx(th,
                       cv2.MORPH_OPEN,
                       np.ones((10, 10), np.uint8),
                       iterations = 4)  

contours, hierarchy = cv2.findContours(th,
                                       cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)

#print(len(contours))
