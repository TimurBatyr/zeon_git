import os
import sys
from os import path

args = sys.argv
# print(args)

BASE_DIR = '.zeon_fs/'


def delfile(args):

    # if len(args) != 2:
    #     print('Should be 1 argument')
    #     exit(0)

    if not path.isfile(f'{BASE_DIR}' + args[1]):
       print('Do not exist such file')
       exit(0)

    if path.isfile(f'{BASE_DIR}' + args[1]):
        os.remove(f'{BASE_DIR}' + args[1])
        print('Deleted')
        exit(0)


if __name__ == '__main__':
    from helper import add_del
    args = sys.argv
    add_del(args)
    delfile(args)
