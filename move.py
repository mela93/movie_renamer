import os
import shutil

dir_path = 'F:/temp/output/'
dstpath = 'F:/temp/output/'


def get_big_file(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            if size > 600 * 1024 * 1024:
                size = size / (1024 * 1024 * 1024)
                size = '{size}G'.format(size=size)
                print(target_file, size)
                move_big_file(target_file)


def move_big_file(srcfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        shutil.move(srcfile, dstpath + fname)
        print("move %s -> %s" % (srcfile, dstpath + fname))


def main():
    get_big_file(dir_path)
    c = input('确认?')
    if c == '':
        print(111)
    else:
        exit()


main()
