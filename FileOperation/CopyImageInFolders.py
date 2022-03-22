import os
import shutil
import sys
from stat import *

SOURCEFOLDER = 'E:\\00_Project\\2022\\DN2130801\\Labels\\zip\\3.21'
TARGETFOLDER = 'E:\\00_Project\\2022\\DN2130801\\Labels\\20220321'


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
    print('Copy file from ' + file + '\r\n---- to ----\r\n' + targetimagepath + '.')


if __name__ == '__main__':
    walktree(SOURCEFOLDER, copyfile)
