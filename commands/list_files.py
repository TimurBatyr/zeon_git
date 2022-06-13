import os
import sys


def listfiles():

    BASE_DIR = '.zeon_fs'

    files_list = os.listdir(BASE_DIR)
    print(f'Files:{len(files_list)}\n')
    for i in files_list:
        print(i)


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    listfiles()






