import os

SOURCEPATH = '../ConvertLabels/data'
TARGETPATH = '../ConvertLabels/data/output'


def walktxt():
    for folderroot, folderlist, filelist in os.walk(SOURCEPATH):
        i = 0
        while i < len(filelist):
            filename = filelist[i]
            if '.txt' not in filename:
                i += 1
                continue
            filewriter = open(os.path.join(SOURCEPATH, filelist[i]), 'a+')
            newfile = ''
            filewriter.seek(0)
            for line in filewriter:
                newline = replaceCRLF(line)
                newfile = newfile + newline
            filewriter.seek(0)
            filewriter.truncate()
            filewriter.write(newfile)
            filewriter.flush()
            filewriter.close()
            i += 1
            print(filename + ': Done.')


def replaceCRLF(line):
    if '\r\n' in line:
        return line
    elif '\r' in line:
        return line.replace('\r', '\r\n')
    elif '\n' in line:
        return line.replace('\n', '\r\n')
    else:
        return line


if __name__ == '__main__':
    walktxt()
