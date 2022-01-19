import zipfile
from zipfile import ZipFile
from pathlib import Path



def extract_imzips(image_dir):
    countfile = 0 
    for image_zip_file in image_dir.iterdir():
        if zipfile.is_zipfile(image_zip_file):
            countfile = countfile + 1

            image_zip_file_name = image_zip_file.stem
            image_zip_file_parent = image_zip_file.parent / image_zip_file_name
            
            if not image_zip_file_parent.exists():
                image_zip_file_parent.mkdir()
                print(f"{image_zip_file_parent} is created")
            
            with ZipFile(image_zip_file) as myzip:
                myzip.extractall(image_zip_file_parent)
            
            countfile = countfile + 1
    return countfile
            



if __name__ == "__main__":
    
    p = Path.cwd()
    countfile = 0 
    for imdir in p.iterdir():
        if imdir.is_dir():
            countfile += extract_imzips(image_dir=imdir)
            
    
    print(f"total files {countfile}")


