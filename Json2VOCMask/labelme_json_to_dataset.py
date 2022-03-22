import json
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from labelme import utils
from skimage import img_as_ubyte
import PIL.Image
import random

JSON_DIR = 'json'
LABELCOLOR = {  # 设定label染色情况
    'product': 1,
}

VOCVersion = 'VOC2012'
Path_VOCDevkit = 'VOCDevkit'
Path_VOC = os.path.join(Path_VOCDevkit, VOCVersion)
Path_Annotations = os.path.join(Path_VOCDevkit, 'Annotations')
Path_ImageSets = os.path.join(Path_VOCDevkit, 'ImageSets')
Path_ImageSets_Action = os.path.join(Path_ImageSets, 'Action')
Path_ImageSets_Layout = os.path.join(Path_ImageSets, 'Layout')
Path_ImageSets_Main = os.path.join(Path_ImageSets, 'Main')
Path_ImageSets_Segmentation = os.path.join(Path_ImageSets, 'Segmentation')
Path_ImageSets_Segmentation_train = os.path.join(Path_ImageSets_Segmentation, 'train.txt')
Path_ImageSets_Segmentation_val = os.path.join(Path_ImageSets_Segmentation, 'val.txt')
Path_JPEGImages = os.path.join(Path_VOCDevkit, 'JPEGImages')
Path_SegmentationClass = os.path.join(Path_VOCDevkit, 'SegmentationClass')
Path_SegmentationObject = os.path.join(Path_VOCDevkit, 'SegmentationObject')


def checkdir():
    createdir(Path_VOCDevkit)
    createdir(Path_VOC)
    createdir(Path_Annotations)
    createdir(Path_ImageSets)
    createdir(Path_ImageSets_Action)
    createdir(Path_ImageSets_Layout)
    createdir(Path_ImageSets_Main)
    createdir(Path_ImageSets_Segmentation)
    createdir(Path_JPEGImages)
    createdir(Path_SegmentationClass)
    createdir(Path_SegmentationObject)


def createdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass


def cvt_one(json_path, save_path_image, save_path_mask, label_color):
    # load img and json
    data = json.load(open(json_path))
    fileName = data['imagePath'][:-4]
    img = utils.image.img_b64_to_arr(data['imageData'])
    PIL.Image.fromarray(img).save(save_path_image)

    lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])

    # get background data
    img = np.zeros([img.shape[0], img.shape[1]])

    # draw roi
    for i in range(len(data['shapes'])):
        name = str(data['shapes'][i]['label'])
        points = data['shapes'][i]['points']
        color = label_color[name]
        img = cv2.fillPoly(img, [np.array(points, dtype=int)], color)
    plt.imshow(img)
    plt.show()
    cv2.imwrite(save_path_mask, img)


def devideDataset(ratio):
    for folderroot, folderlist, filelist in os.walk(Path_SegmentationClass):
        seglist = []
        i = 0
        while i < len(filelist):
            if '.png' in filelist[i]:
                seglist.append(filelist[i][:-4])
            i += 1
        random.shuffle(seglist)
        offset = int(ratio * len(seglist))
        train_list = seglist[offset:]
        val_list = seglist[:offset]
        writeTxt(Path_ImageSets_Segmentation_train, train_list)
        writeTxt(Path_ImageSets_Segmentation_val, val_list)

def writeTxt(filePath, namelist):
    file = open(filePath, 'w+')
    file.seek(0)
    for name in namelist:
        file.write(name + '\n')
    file.flush()
    file.close()


if __name__ == '__main__':
    checkdir()

    for folderroot, folderlist, filelist in os.walk(JSON_DIR):
        jsonfilelist = []
        i = 0
        while i < len(filelist):
            if '.json' in filelist[i]:
                jsonfilelist.append(filelist[i])
            i += 1

    for i in range(len(jsonfilelist)):
        json_path = os.path.join(JSON_DIR, jsonfilelist[i])

        save_path_image = os.path.join(Path_JPEGImages, jsonfilelist[i].replace('.json', '.jpg'))
        save_path_mask = os.path.join(Path_SegmentationClass, jsonfilelist[i].replace('.json', '.png'))

        print('Processing {}'.format(json_path))

        cvt_one(json_path, save_path_image, save_path_mask, LABELCOLOR)

    devideDataset(0.3)
