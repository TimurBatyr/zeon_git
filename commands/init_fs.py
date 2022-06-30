import os
import sys
from os import path
from pathlib import Path


BASE_DIR = os.path.abspath(os.path.curdir)+ '/.zeon_git'
DATABASE_PATH = f'{BASE_DIR}/index.txt'
OBJECTS_PATH = f'{BASE_DIR}/objects'

def initfs():

    if path.isdir(OBJECTS_PATH):
        print('Such dir exists')
        # exit(0)

    if not path.isdir(OBJECTS_PATH):
        os.makedirs(OBJECTS_PATH)
        print('Created')
        # exit(0)


def initdb():
    if not Path(DATABASE_PATH).exists():
        Path(DATABASE_PATH).touch()
        print('Database was initialized')
        exit(0)
    print('Database already exists')


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    initfs()
    initdb()