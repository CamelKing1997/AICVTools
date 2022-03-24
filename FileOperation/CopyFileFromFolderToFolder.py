import os
import shutil
import sys
from stat import *
import argparse

def walkfolder(srcdir, tardir):
    index = 1
    for root, dirs, files in os.walk(srcdir, True):
        for file in files:
            shutil.copy(os.path.join(root, file), tardir)
            index += 1
            print(f'[num:{index:}] COPY {os.path.join(root, file)}    TO    {os.path.join(tardir, file)}')

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--srcdir', type=str, default='')
    parser.add_argument('--tardir', type=str, default='')
    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    opt = parse_opt()
    srcdir = opt.srcdir
    tardir = opt.tardir
    walkfolder(srcdir, tardir)
