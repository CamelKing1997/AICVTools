import os
import shutil
import sys
from PIL import Image
import argparse

imgType_list = {'jpg', 'bmp', 'png', 'jpeg', 'tif'}


def walkfolder(srcdir):
    index = 1
    for root, dirs, files in os.walk(srcdir, True):
        for file in files:
            if file[-3:] in imgType_list:
                imagepath = os.path.join(root, file)
                image = Image.open(imagepath)
                imagesavepath = os.path.join(root, file[:-3]+"jpg")
                image.save(imagesavepath, quality=95)

                index += 1
                print(f'[NUM:{index:}] {os.path.join(root, file)} CONVERTED.')

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--srcdir', type=str, default='E:\\00_Project\\2022\\DN2130801\\DailyImages\\0323')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    srcdir = opt.srcdir
    walkfolder(srcdir)
