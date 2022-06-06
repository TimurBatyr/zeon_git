import os
import sys
from os import path

def initfs():
    args = sys.argv
    print(args)

    BASE_DIR = 'zeon_fs2'

    if len(args) != 1:
        print('Should be no argument')
        # exit(0)

    if path.isdir(BASE_DIR):
        print('Such dir exists')
        exit(0)

    if not path.isdir(BASE_DIR):
        os.mkdir(BASE_DIR)
        print('Created')
        exit(0)

if __name__ == '__main__':
    initfs()