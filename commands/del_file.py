import os
import shutil
import sys
from os import path
from pathlib import Path

args = sys.argv
# print(args)

BASE_DIR = '.zeon_git'


def delfile(args):
    full_path = (BASE_DIR+ f'/{args[1].lstrip("/")}')

    if len(args) <= 2:

        # if file
        # os.remove(file)
        #shutil.rm

        if not path.isdir(full_path):
            if not path.isfile(full_path):
                print('Does not exist such file or dir')
                return 0
            os.remove(full_path)
            print('File deleted')
            return 0
        shutil.rmtree(full_path)
        print('Dir deleted')
        return 0

if __name__ == '__main__':
    from helper import del_file
    args = sys.argv
    del_file(args)
    delfile(args)