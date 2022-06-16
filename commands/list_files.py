import os
import sys


def listfiles():

    BASE_DIR = '.zeon_git'

    # files_list = os.listdir(BASE_DIR)
    # print(f'Files:{len(files_list)}\n')
    # for i in files_list:
    #     print(i)
    for root, dirs, files in os.walk(BASE_DIR, topdown=True):
        # for name in files:
        #     print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
        print(f'Path: {root}')
        print(f'Directories: {dirs}')
        print(f'Files: {files}')
        print('--------------------------------')


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    listfiles()






