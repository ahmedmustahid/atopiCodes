import pandas as pd
from pathlib import Path
import sys
import re


if __name__=="__main__":
    
    dfWithValues = pd.read_csv("/home/ahmed/work/atopiWork/atopiCodes/preprocessing/csvs/preprocessed_file.csv")
    filteredDfWithValues = dfWithValues[["patientNumber", "degradation rate"]][:10]
    
    patientNumberList = dfWithValues["patientNumber"].to_list()
    patientNumberDict = dict.fromkeys(patientNumberList)
    patientNumberDegradationDict = {key:int(value) for key, value in zip(patientNumberDict.keys(), dfWithValues["degradation rate"])}
    #patientNumberDegradationDict = {key:[int(value)] for key, value in zip(patientNumberDict.keys(), dfWithValues["degradation rate"])}
    

    atopiImagesPath = Path("/home/ahmed/work/atopiWork/atopiImagesSkinOnly/masks")
    
    dictForDf = {"patientNumber":[],"imagePath":[],"degradationRate":[]}
    for imagePath in atopiImagesPath.iterdir():

        if imagePath.suffix==".jpeg" or imagePath.suffix==".jpg" or imagePath.suffix==".png" or imagePath.suffix==".JPG":
            imageName = imagePath.name
            patientNumber = imageName.split("-")[1]
            patientNumber = int(re.sub(r"[^0-9]","",patientNumber))

            if patientNumber in patientNumberDegradationDict:
                dictForDf["patientNumber"].append(patientNumber)
                dictForDf["imagePath"].append(str(imagePath))
                dictForDf["degradationRate"].append(patientNumberDegradationDict[patientNumber])
        
        #break

    df = pd.DataFrame.from_dict(dictForDf)
    print(df)
    df.to_csv("patientNumber_imName_DegradationRate.csv")




