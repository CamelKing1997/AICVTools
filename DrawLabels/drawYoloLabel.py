import os
from tqdm import tqdm
import cv2
import numpy as np

ROOT = 'E:/00_Project/2022/Tools/PythonCVTools'
DATAPATH = '../DrawLabels/data/20220316'
OutputPath = os.path.join(DATAPATH, 'Drawed')
# classestxt = ['scratch']


def drawLabel():
    for folderroot, folderlist, filelist in os.walk(DATAPATH):
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
            filereader = open(os.path.join(DATAPATH, labelfile + '.txt'), 'rb')
            filereader.seek(0)
            labellist = []
            for line in filereader:
                line = removeCRLF(line)
                labellist.append(line)
            filereader.seek(0)
            filereader.flush()
            filereader.close()

            # Read Image
            img = cv2.imread(os.path.join(DATAPATH, labelfile + '.jpg'))
            size = img.shape  # hwc
            imgh, imgw = size[0], size[1]
            # Test Output Folder
            if not os.path.exists(OutputPath):
                os.makedirs(OutputPath)
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
                confidence = randomConfidence()
                l = 'scratch:' + '%.2f' % confidence
                p1 = (int(x1), int(y1))
                p2 = (int(x2), int(y2))
                cv2.rectangle(img, p1, p2, (0, 0, 255), 3)
                # cv2.putText(img, l, (int(x1), int(y1) - 8), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
                filename = os.path.join(OutputPath, labelfile + '.jpg')
                cv2.imwrite(filename, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


def removeCRLF(line):
    line = line.decode()
    if '\r\n' in line:
        line = line.removesuffix('\r\n')
    elif '\r' in line:
        line = line.removesuffix('\r')
    elif '\n' in line:
        line = line.removesuffix('\n')
    else:
        pass
    return line


def randomConfidence():
    return np.random.uniform(0.6, 0.85)


if __name__ == '__main__':
    drawLabel()
