import os
import sys


def listfiles():

    BASE_DIR = '.zeon_git'
    # for root, dirs, files in os.walk(BASE_DIR, topdown=True):
    #     # for name in files:
    #     #     print(os.path.join(root, name))
    #     # for name in dirs:
    #     #     print(os.path.join(root, name))
    #     print(f'Path: {root}')
    #     print(f'\tDirectories: {dirs}')
    #     print(f'\t\tFiles: {files}')
    #     print('--------------------------------')

    for dirpath, dirnames, filenames in os.walk(BASE_DIR):
        directory_level = dirpath.replace(BASE_DIR, "")
        directory_level = directory_level.count(os.sep)
        indent = " " * 4
        # print("{}{}/".format(indent * directory_level, os.path.basename(dirpath)))
        print(f'{indent * directory_level} {os.path.basename(dirpath)}/')

        for f in filenames:
            print("{}{}".format(indent * (directory_level + 1), f))


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    listfiles()






