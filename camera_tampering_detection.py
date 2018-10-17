
# coding: utf-8

# In[5]:


import numpy as np
import cv2
cap = cv2.VideoCapture('path to the video file')
fgbg = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
fgmask = fgbg.apply(frame)
kernel = np.ones((5,5), np.uint8) 
while(True):
    ret, frame = cap.read()
    if(frame is None):
        print("End of frame")
        break;
    else:
        a = 0
        bounding_rect = []
        fgmask = fgbg.apply(frame)
        fgmask= cv2.erode(fgmask, kernel, iterations=5) 
        fgmask = cv2.dilate(fgmask, kernel, iterations = 5)
        cv2.imshow('frame',frame)
        _,contours,_ = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):
            bounding_rect.append(cv2.boundingRect(contours[i]))
        for i in range(0,len(contours)):
            if bounding_rect[i][2] >=40 or bounding_rect[i][3] >= 40:
                a = a+(bounding_rect[i][2])*bounding_rect[i][3]
            if(a >=int(frame.shape[0])*int(frame.shape[1])/3):
                cv2.putText(frame,"TAMPERING DETECTED",(5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)   
            cv2.imshow('frame',frame)        
               
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

