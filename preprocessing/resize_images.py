import cv2
from pathlib import Path
import os

imOriginalRootPath = Path.home()/'work'/'atopiWork/atopZips'
resizedImagePathRoot = imOriginalRootPath.parent/"atopiImages_256x256"

allImsList = list(imOriginalRootPath.rglob("*.jpeg")) + list(imOriginalRootPath.rglob("*.jpg")) + list(imOriginalRootPath.rglob("*.JPG")) + list(imOriginalRootPath.rglob("*.png"))

print(len(allImsList))

print("/".join(allImsList[0].parts[6:]))

for i,imagePath in enumerate(allImsList):
    #print(imagePath)
    #print("imagepath")
    actualImage = cv2.imread(str(imagePath), cv2.IMREAD_UNCHANGED)
    #print(actualImage.shape)
    resizedImageDimension = (256, 256)
    resizedImage = cv2.resize(actualImage, resizedImageDimension, interpolation= cv2.INTER_AREA)
    #print(resizedImage.shape)

    resizedImagePath = resizedImagePathRoot/"-".join(imagePath.parts[6:])
    resizedImageNameWithNewExtension = resizedImagePath.stem + ".png"

    #resizedImagePathWithExtensionParent =  resizedImagePath.parent
    #print(resizedImagePathWithExtensionParent)
    #if not resizedImagePathWithExtensionParent.exists():
    #    os.makedirs(str(resizedImagePathWithExtensionParent)) 
    #resizedImagePathWithExtension = resizedImagePathWithExtensionParent/resizedImageNameWithNewExtension
    
    #print("resizedPath ")
    #print(resizedImagePath)
    #print(resizedImagePathWithExtension)
    print("imagenumber ", i + 1)
    cv2.imwrite(str(resizedImagePath),resizedImage)

    #if i==5:
    #    break
    #print(resizedImagePathWithExtension)
    #print(resizeImagePath)

