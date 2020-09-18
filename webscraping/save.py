from urllib.request import Request,urlopen
import csv
import os
import pathlib
import shutil
from glob import glob
import pandas as pd

SAVE_DIRECTORY= pathlib.Path(r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\RawImages_Wrinkles')

def saveFile(index,url):
    path = os.path.join(SAVE_DIRECTORY,"img_"+str(index)+".jpg")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response, open(path,'wb') as out_file:
        shutil.copyfileobj(response,out_file)

# SAVE_DIRECTORY.mkdir(parents=True,exist_ok=True)
# file_name = 'wrinkle_dataset_2xlarge.csv'
# os.chdir('FYPSkinMeasure\webscraping')
# with open(file_name) as csv_file:
#     readCsv = csv.reader(csv_file,delimiter=',')
#     next(readCsv,None)
#     for row in readCsv:
#         saveFile(row[0],row[1])

## combine csv together
def combineCsv():
    extension = 'csv'
    all_filenames = [i for i in glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


# combineCsv()

def dropColumn():
    path = pathlib.Path(r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\Dataset [Clean]\dataset_final.csv')

    readCsv = pd.read_csv(path)
    readCsv = readCsv.drop('id',1)
    readCsv.to_csv(path)

dropColumn()