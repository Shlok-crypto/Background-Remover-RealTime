import cv2 as cv
import numpy as np
import time

def background_Change_Remove():
    capture = cv.VideoCapture(0)
    x = 0.5
    y = 0.8
    def temps(x):
        pass

    # Background Image(Pre-Saved)
   # NewBackGroundframe = cv.imread(r'') # add the Path New Background image
   # NewBackGroundframe = NewBackGroundframe[0:384, 0: 320]  # croping the New Background

# New Background image, captured From Webcam
    _, NewBackGroundframe = capture.read()
    NewBackGroundframe = NewBackGroundframe[0:int(y * NewBackGroundframe.shape[0]), int(x * NewBackGroundframe.shape[1]): NewBackGroundframe.shape[1]]
    NewBackGroundframe = cv.flip(NewBackGroundframe, 1)

    time.sleep(2)

    # Creating Trackbar Window
    bars = cv.namedWindow("bars")
    cv.createTrackbar("thresh", "bars", 175, 255, temps)
    cv.createTrackbar("convlaue", "bars",50, 1000, temps)


    while True:
         _,frame2 = capture.read()

         # Cliping ROI
         img = frame2[0:int(y * frame2.shape[0]), int(x * frame2.shape[1]): frame2.shape[1]]
         img = cv.flip(img, 1)
         print(img.shape)
         cv.imshow("ROI",img)

         mask = np.zeros_like(img)
         OutlineMask = np.zeros_like(img)

         grayFrame = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
         Blur = cv.GaussianBlur(grayFrame,(5,5),0)

    # Getting the values
         threshh = cv.getTrackbarPos("thresh", "bars")
         convaluee = cv.getTrackbarPos("convlaue", "bars")

    #threshold the frame
         _,thresh = cv.threshold(Blur,threshh,255,cv.THRESH_BINARY)

   # Dilation of the thresh
         dilation = cv.dilate(thresh,None,iterations=3)

    #find the contours(Boundry of the object)
         contour, hierarchies = cv.findContours(dilation, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
         for c in contour:
            if  cv.contourArea(c) < convaluee:
                continue

            hull = cv.convexHull(c)
            cv.drawContours(mask,contour,-1, (255,255,255),-1) # Fill the CONTOUR WHITE

            cv.drawContours(OutlineMask, c, -1, (0, 255, 0), 3)  # DRAW CONTOURS
            cv.drawContours(OutlineMask, [hull], 0, (0, 0, 255), 2) # DRAW TIGHT FITTING BOUNDARY

            # Separate ROI from Background
            img = cv.bitwise_and(img,mask)

            # Invers the mask(BlACK => white & WHITE => black)
            _, InvMask = cv.threshold(mask, threshh, 255, cv.THRESH_BINARY_INV)
            cv.imshow("INVMASk",InvMask)

            # Overlay Mask onto NEW BACKGROUND
            NewBackGround = cv.bitwise_and(NewBackGroundframe,InvMask)

            # Combine NewBackGround and ROI
            finalFrame = cv.bitwise_or(NewBackGround,img)


         cv.imshow("ForGround",img)
         cv.imshow("Draw",OutlineMask)
         cv.imshow("dil",thresh)
         cv.imshow('NewBackGround', NewBackGroundframe)
         cv.imshow('FinalIMAG',finalFrame)

         if cv.waitKey(45) == ord('q'):
             break
    capture.release()
    cv.destroyAllWindows()

