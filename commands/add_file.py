import shutil
import sys
from os import path
from pathlib import Path


def addfile(args):

    BASE_DIR = 'zeon_fs2/'

    # if len(args) != 2:
    #     print('Should be 2 arguments')
    #     exit(0)

    if not path.isfile(args[1]):
        print('It is not a file')
        exit(0)

    file_name = Path(args[1]).name

    if path.isfile(f'{BASE_DIR}' + file_name):
        print('Already exists file')
        exit(0)

    shutil.copyfile(args[1], f'{BASE_DIR}' + file_name)


if __name__ == '__main__':
    from repeated_code import add_del
    args = sys.argv
    add_del(args[1:])
    addfile(args)
