from pathlib import Path
import re
import sys
import pandas as pd
import shutil

atopiRoot = Path.home()/"work/atopiWork"

atopiResultsDir = atopiRoot/"results_atopi_skinSegmentation/results"
copyNameFromDir = atopiRoot/"results_atopi_skinSegmentation/accurate"

copyFromDir = atopiRoot/"masks_atopi_skinSegmentation/masks"
copyToDir = atopiRoot/"masks_atopi_skinSegmentation/accurate"

copyNameFromFiles = [re.sub("results","mask",f.name) for f in copyNameFromDir.rglob("*") if f.suffix==".jpg" or f.suffix==".jpeg" or f.suffix==".png"]
df = pd.DataFrame(data={"copyNameOnly":copyNameFromFiles})


for copyFile in df["copyNameOnly"]:
    
    copyFromDirFilePath = copyFromDir/copyFile
    #copyToDirFilePath = copyToDir/copyFile

    if copyFromDirFilePath.exists():
        print(copyFromDirFilePath)
        shutil.copy(copyFromDirFilePath, copyToDir)



