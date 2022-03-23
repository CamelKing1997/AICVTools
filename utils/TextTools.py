
class TextTools():
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