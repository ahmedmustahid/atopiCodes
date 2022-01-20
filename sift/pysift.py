import numpy as np
import cv2 as cv
from pathlib import Path


impaths = Path('/home/ahmed/work/atopiWork/worstSkin')

for imfilepath in impaths.iterdir():
    
    if imfilepath.is_file():
    
        img = cv.imread(str(imfilepath))
        imgWithKeypoints = img.copy()
        #gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        sift = cv.SIFT_create()
        kp = sift.detect(img,None)
        #kp = sift.detect(gray,None)
        img=cv.drawKeypoints(img,kp,imgWithKeypoints)
        
        imfilepathResultDir = imfilepath/"siftresults"
        imfilepathName = imfilepath.stem 
    
        finalDir = imfilepathResultDir/imfilepathName
        print(finalDir)
        cv.imwrite(str(finalDir)+".jpg",imgWithKeypoints)
