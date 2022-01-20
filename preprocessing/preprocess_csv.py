from pathlib import Path
import os
import pandas as pd

def select_men_bad_skin(df):

    df_new = df[(df["degradation rate"]=="5") & (df["gender"]=="m") ]
    return df_new


df = pd.read_csv("csvs/preprocessed_file.csv")
df_new = select_men_bad_skin(df)
#print(df_new)

for _, row in df_new["patientNumber"].iteritems():
    #print(row)
    for root, dirs, files in os.walk("/home/ahmed/work/atopiWork/atopZips"):
    
        for directory in dirs:
            if directory == str(row):
                print("inside")
                print(root+"/"+directory)
                dirlist = os.listdir(root+"/"+directory)
                print(*dirlist,sep="\n")
                break
