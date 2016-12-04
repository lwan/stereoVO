import numpy as np
import cv2
import operator

def getFeatures(img, sizeWindowArray ):
    
    height, width= img.shape

    xstep = int(width/sizeWindowArray[1])
    ystep = int(height/sizeWindowArray[0])
    arrayidx = 0
    sift = cv2.xfeatures2d.SIFT_create(100)
    windowidx = 0
    for y in range(0,ystep*sizeWindowArray[0],ystep):

        for x in range(0,xstep*sizeWindowArray[1],xstep):
            kpTemp = sift.detect(img[y:y+ystep-1,x:x+xstep-1],None)
            
            for idx in range(len(kpTemp)):
                kpTemp[idx].pt = tuple(map(operator.add,  kpTemp[idx].pt, (x,y)))
            
            if windowidx == 0:
                kp = kpTemp
                windowidx = 1
                continue
           
            kp = kp + kpTemp

    return kp


