from PIL import Image
from torch.utils.data import Dataset, DataLoader
import numpy as np

import glob
import pathlib
import os
import csv

# raw_path = pathlib.Path(r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\img_dataset_kaggle23_03\skin-lesion-segmentation\testx')
raw_path = pathlib.Path(
    r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\CroppedImages_Wrinkles')
clean_path = pathlib.Path(
    r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\GrayscaledImages_Wrinkles')

# Convert images in the dataset to grayscale (3 channels -> 1 channel)


def toGrayscale():
    clean_path.mkdir(parents=True, exist_ok=True)

    images = [str(pp) for pp in raw_path.glob("**/*.jpg")]

    for index, image in enumerate(images):
        count = index+1
        with open(image, 'rb') as file:
            temp = Image.open(file).convert('L')
            file_name = "g_img"+str(count)+".jpg"
            file_path = os.path.join(clean_path, file_name)
            temp.save(file_path)
            print("Saved "+file_path)

# toGrayscale()


# create image-label dataset in csv format
""" 
Directory for tensor labels
1 -- Lesions
2 -- Wrinkles
etc.
"""

print(os.getcwd())


def compileImagestoCSV():
    # collection_path = ''
    csv_path = pathlib.Path(
        r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\Dataset [Clean]\grayscaled_resized_lesions_2')
    images = [str(pp) for pp in csv_path.glob("**/*.jpg")]
    os.chdir(csv_path)
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'path', 'label'])
        for index, image in enumerate(images):
            writer.writerow([index, image, 1])

# compileImagestoCSV()

# resize all images to 64x64


def resizeToInput():

    read_path = pathlib.Path(
        r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\clean_test_1')
    save_path = pathlib.Path(
        r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\Dataset [Clean]\test2')
    save_path.mkdir(parents=True, exist_ok=True)
    images = [str(pp) for pp in read_path.glob("**/*.jpg")]

    for index, image in enumerate(images):
        count = index+1
        with open(image, 'rb') as file:
            temp = Image.open(file)
            temp = temp.resize((64, 64))
            file_name = "g_img"+str(count)+".jpg"
            file_path = os.path.join(save_path, file_name)
            temp.save(file_path)
            print("Saved "+file_path)
# resizeToInput()
