import pandas as pd
from pathlib import Path


nonAtopiImagesPath = Path("/home/ahmed/work/atopiWork/masks_NonAtopiImages")
currentDir = Path.cwd()
csvPath = currentDir/"csvs"
#pathGenerator = (filePath for filePath in nonAtopiImagesPath.glob("*.jpeg"))
#print(list(pathGenerator))
#print(list(0 for _ in pathGenerator))
pathList =[str(filePath) for filePath in nonAtopiImagesPath.glob("*.jpeg")] 
atopiPathDict = {"imagePath":pathList,"label":list(0 for _ in pathList)}

print(atopiPathDict)
nonAtopiDf = pd.DataFrame(data=atopiPathDict)
nonAtopiDf.to_csv(str(csvPath)+"/"+"nonAtopiImagesList.csv")

print(nonAtopiDf)


