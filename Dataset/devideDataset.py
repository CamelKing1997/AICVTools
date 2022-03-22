import os
import shutil
import random
from tqdm import tqdm

ROOT = 'E:/00_Model/Yolo/v5/yolov5'
ROOTDATASETPATH = 'Project/DN2130801/dataset/'

SOURCEPATH = 'Project/DN2130801/dataset/side/all'
IMAGESPATH = 'Project/DN2130801/dataset/side/images'
LABELSPATH = 'Project/DN2130801/dataset/side/labels'


def devideDataset(ratio):
    for folderroot, folderlist, filelist in os.walk(PATH):
        list = []
        i = 0
        while i < len(filelist):
            list.append(filelist[i][:-4])
            i += 2
        random.shuffle(list)
        offset = int(ratio * len(list))
        train_list = list[offset:]
        val_list = list[:offset]
        if not os.path.exists(os.path.join(ROOT, IMAGESPATH, 'train')):
            os.makedirs(os.path.join(ROOT, IMAGESPATH, 'train'))
        if not os.path.exists(os.path.join(ROOT, IMAGESPATH, 'val')):
            os.makedirs(os.path.join(ROOT, IMAGESPATH, 'val'))
        if not os.path.exists(os.path.join(ROOT, LABELSPATH, 'train')):
            os.makedirs(os.path.join(ROOT, LABELSPATH, 'train'))
        if not os.path.exists(os.path.join(ROOT, LABELSPATH, 'val')):
            os.makedirs(os.path.join(ROOT, LABELSPATH, 'val'))
        for file in tqdm(val_list):
            sourceimagepath = os.path.join(ROOT, SOURCEPATH, file + '.jpg')
            sourcelabelpath = os.path.join(ROOT, SOURCEPATH, file + '.txt')
            targetimagepath = os.path.join(ROOT, IMAGESPATH, 'val', file + '.jpg')
            targetlabelpath = os.path.join(ROOT, LABELSPATH, 'val', file + '.txt')
            shutil.copy(sourceimagepath, targetimagepath)
            shutil.copy(sourcelabelpath, targetlabelpath)
        for file in tqdm(train_list):
            sourceimagepath = os.path.join(ROOT, SOURCEPATH, file + '.jpg')
            sourcelabelpath = os.path.join(ROOT, SOURCEPATH, file + '.txt')
            targetimagepath = os.path.join(ROOT, IMAGESPATH, 'train', file + '.jpg')
            targetlabelpath = os.path.join(ROOT, LABELSPATH, 'train', file + '.txt')
            shutil.copy(sourceimagepath, targetimagepath)
            shutil.copy(sourcelabelpath, targetlabelpath)

PATH = 'E:/00_Project/2022/DN2130801/Labels/20220317NG'
def modifyDataset():
    for folderroot, folderlist, filelist in os.walk(PATH):
        i = 0
        while i < len(filelist):
            filename = filelist[i]
            if '.txt' not in filename:
                i += 1
                continue
            filewriter = open(os.path.join(PATH, filelist[i]), 'a+', encoding='utf-8')
            newfile = ''
            filewriter.seek(0)
            for line in filewriter:
                if len(line) >= 4:
                    newline = "0" + line[1:]
                    newfile = newfile + newline
            filewriter.seek(0)
            filewriter.truncate()
            filewriter.write(newfile)
            filewriter.flush()
            filewriter.close()
            i += 1
            print(filename + ': Done.')


if __name__ == '__main__':
    # devideDataset(0.3)
    modifyDataset()
