import os
from tqdm import tqdm
import cv2
from utils.TextTools import TextTools


SOURCE_DIR = 'E:\\00_Project\\2022\\DN2130801\\Labels\\20220322_lhc'
TARGET_DIR = 'E:\\00_Project\\2022\\DN2130801\\DataStatistic\\20220322_LHC'


def LabelStatistic(path, output):
    for folderroot, folderlist, filelist in os.walk(path):
        list = []
        i = 0
        while i < len(filelist):
            if '.txt' in filelist[i]:
                if filelist[i][:-4] == 'classes':
                    i += 1
                    continue
                list.append(filelist[i][:-4])
            i += 1
    for labelfile in tqdm(list):
        # Read Labels
        filereader = open(os.path.join(path, labelfile + '.txt'), 'rb')
        filereader.seek(0)
        labellist = []
        for line in filereader:
            line = TextTools.removeCRLF(line)
            labellist.append(line)
        filereader.seek(0)
        filereader.flush()
        filereader.close()

        # Read Image
        img = cv2.imread(os.path.join(path, labelfile + '.jpg'))
        size = img.shape  # hwc
        imgh, imgw = size[0], size[1]
        # Test Output Folder
        if not os.path.exists(output):
            os.makedirs(output)
        # Draw Label on Image
        for label in labellist:
            label = label.split(' ')
            k = label[0]
            x = float(label[1]) * imgw
            y = float(label[2]) * imgh
            w = float(label[3]) * imgw
            h = float(label[4]) * imgh
            x1, x2 = x - w / 2, x + w / 2
            y1, y2 = y - h / 2, y + h / 2
            p1 = (int(x1), int(y1))
            p2 = (int(x2), int(y2))
            cv2.rectangle(img, p1, p2, (0, 0, 255), 3)
            filename = os.path.join(output, labelfile + '.jpg')
            cv2.imwrite(filename, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

if __name__ == '__main__':
    LabelStatistic(SOURCE_DIR, TARGET_DIR)
