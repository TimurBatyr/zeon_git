import os
import sys
from os import path

args = sys.argv
# print(args)

BASE_DIR = '.zeon_fs/'


def delfile(args):

    if not path.isfile(f'{BASE_DIR}' + args[1]):
       print('Do not exist such file')
       exit(0)

    if path.isfile(f'{BASE_DIR}' + args[1]):
        os.remove(f'{BASE_DIR}' + args[1])
        print('Deleted')
        exit(0)


if __name__ == '__main__':
    from helper import del_file
    args = sys.argv
    del_file(args)
    delfile(args)
