import os
import sys


def listfiles():

    BASE_DIR = '.zeon_git'
    for root, dirs, files in os.walk(BASE_DIR, topdown=True):
        # for name in files:
        #     print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
        print(f'Path: {root}')
        print(f'\tDirectories: {dirs}')
        print(f'\t\tFiles: {files}')
        print('--------------------------------')


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    listfiles()






