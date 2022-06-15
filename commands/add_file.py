import os
import shutil
import sys
from os import path
from pathlib import Path


def addfile(args):

    BASE_DIR = '.zeon_fs'
    file_name = Path(args[1]).name

    if len(args) <= 2:
        if not path.isfile(args[1]):
            print('It is not a file')
            exit(0)
        elif path.isfile(BASE_DIR + f'/{file_name}'):
            print('Already exists file')
            exit(0)
        shutil.copyfile(args[1], BASE_DIR + f'/{file_name}')
        print('Added a file')

    elif len(args) <= 3:
        make_dir = args[2]
        path_to = (os.path.join(BASE_DIR, make_dir.lstrip('/')))

        os.makedirs(Path(path_to).parent, exist_ok=True)
        if not path.isfile(args[1]):
            print('Does not exist such file')
            exit(0)

        # elif path.isfile(BASE_DIR + f'/{args[2]}/{file_name}'):
        elif path.isfile(f'{path_to}/{file_name}'):
            print('Already exists file')
            exit(0)

        # shutil.copyfile(args[1], f'{Path(path_to).parent}/{Path(path_to).name}')
        shutil.copyfile(args[1], path_to)
        print('Added a file')


if __name__ == '__main__':
    from helper import add_file
    args = sys.argv
    add_file(args)
    addfile(args)
