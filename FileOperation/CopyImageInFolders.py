import os
import shutil
import sys
from stat import *
import argparse

SOURCEFOLDER = 'E:\\00_Project\\2022\\DN2130801\\Dataset\\LHC\\yolo-3.22'
TARGETFOLDER = 'E:\\00_Project\\2022\\DN2130801\\Labels\\20220322_lhc'


def walktree(top, callback):
    """walk file tree from position top,
    for each file, callback is called."""
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        try:
            mode = os.stat(pathname, follow_symlinks=False).st_mode
        except:
            continue
        if S_ISDIR(mode):
            # directory, recurse into it
            walktree(pathname, callback)
        else:
            # file, whatever type, make the call back function
            callback(pathname)
    return


def copyfile(file):
    filename = os.path.basename(file)
    targetimagepath = os.path.join(TARGETFOLDER, filename)
    shutil.copy(file, targetimagepath)
    print('Copy file from ' + file +  ' to ' + targetimagepath + '.')

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--srcdir', type=str, default='E:\\00_Project\\2022\\DN2130801\\Dataset\\LHC\\yolo-3.22')
    parser.add_argument('--tardir', type=str, default='E:\\00_Project\\2022\\DN2130801\\Labels\\20220322_lhc')
    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    opt = parse_opt()
    SOURCEFOLDER = opt.srcdir
    TARGETFOLDER = opt.tardir
    walktree(SOURCEFOLDER, copyfile)
