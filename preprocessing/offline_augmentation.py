import numpy as np
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import cv2
from scipy.ndimage.interpolation import rotate
from pathlib import Path


class AugmentImage:
    def __init__(self, image, angleRange=(25,180)):
        self.image = image
        self.angleRange = angleRange

    def flipImage(self):
        return self.image[:,::-1,:]

    def verticalFlip(self):
        return self.image[::-1, :, :]

    def randomRotation(self):
        h, w, _ = self.image.shape
        angle = np.random.randint(*self.angleRange)
        image = rotate(self.image, angle)
        image = cv2.resize(image, (h,w), cv2.INTER_AREA)
        return image
   

    def applyGaussianNoise(self):
        image = self.image /255
        mu, sigma = 0, 0.1
        gaussian =  np.random.normal(mu, sigma, image.shape)
        return np.where(image==0, image, image + gaussian) * 255
    

def augmentImagePipeLine(imagesPath, augmentationType):

    for imagePath in imagesPath.glob("*.jpeg"):
        imagePath = Path(imagePath)
        imagePathParent = imagePath.parent 
        imageName = imagePath.name.split(".")[0]

        newImageName = imageName+"_"+augmentationType+".jpeg"
        newImagePath = imagePathParent/newImageName
        
        image = cv2.imread(str(imagePath),cv2.IMREAD_UNCHANGED)
        augmentImage = AugmentImage(image)
        
        if augmentationType=="horizontalFlip":
            augmentedImage = augmentImage.flipImage()
        elif augmentationType=="verticalFlip":
            augmentedImage = augmentImage.verticalFlip()

        elif augmentationType=="gaussianNoise":
            augmentedImage = augmentImage.applyGaussianNoise()
        
        elif augmentationType=="randomRotation":
            augmentedImage = augmentImage.randomRotation()
            

        #flippedImage = cv2.cvtColor(flippedImage,cv2.COLOR_BGR2RGB)
        cv2.imwrite(str(newImagePath),augmentedImage)
        print(str(newImagePath))




if __name__=="__main__":

    #dfNonAtopi= pd.read_csv("/home/ahmed/work/atopiWork/atopiCodes/preprocessing/csvs/nonAtopiImagesList.csv")
    
    #for imagePath in dfNonAtopi["imagePath"]:
    #    #print(imagePath)
    #    imagePath = Path(imagePath)
    #    imagePathParent = imagePath.parent 
    #    imageName = imagePath.name.split(".")[0]

    #    newImageName = imageName+"_flipped"+".jpeg"
    #    newImagePath = imagePathParent/newImageName
    #    
    #    image = cv2.imread(str(imagePath),cv2.IMREAD_UNCHANGED)
    #    augmentImage = AugmentImage(image)
    #    flippedImage = augmentImage.flipImage()

    #    #flippedImage = cv2.cvtColor(flippedImage,cv2.COLOR_BGR2RGB)
    #    cv2.imwrite(str(newImagePath),flippedImage)

    imagesPath = Path("/home/ahmed/work/atopiWork/masks_NonAtopiImages/")
    augmentImagePipeLine(imagesPath=imagesPath, augmentationType="horizontalFlip")
    augmentImagePipeLine(imagesPath=imagesPath, augmentationType="verticalFlip")
    augmentImagePipeLine(imagesPath=imagesPath, augmentationType="randomRotation")
    augmentImagePipeLine(imagesPath=imagesPath, augmentationType="gaussianNoise")





