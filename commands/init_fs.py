import os
import sys
from os import path


def initfs():
    BASE_DIR = os.path.abspath(os.path.curdir)+ '/.zeon_fs'

    # if len(args) != 1:
    #     print('Should be no argument')
        # exit(0)

    if path.isdir(BASE_DIR):
        print('Such dir exists')
        exit(0)

    if not path.isdir(BASE_DIR):
        os.mkdir(BASE_DIR)
        print('Created')
        exit(0)


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    initfs()
