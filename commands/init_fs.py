import os
import sys
from os import path
from pathlib import Path


BASE_DIR = os.path.abspath(os.path.curdir)+ '/.zeon_git'
DATABASE_PATH = f'{BASE_DIR}/index.txt'
OBJECTS_PATH = f'{BASE_DIR}/objects'

HOOKIES_PATHS = [
    os.path.abspath(os.path.curdir) + f'/hookies/add/pre_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/add/post_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/del/pre_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/del/post_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/list/pre_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/list/post_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/init/pre_hook',
    os.path.abspath(os.path.curdir) + f'/hookies/init/post_hook',
]

def initfs():

    if path.isdir(OBJECTS_PATH):
        print('Such dir already exists')

    if not path.isdir(OBJECTS_PATH):
        os.makedirs(OBJECTS_PATH)
        print('Created')


def initdb():
    if not Path(DATABASE_PATH).exists():
        Path(DATABASE_PATH).touch()
        print('Database was initialized')
        exit(0)
    print('Database already exists')


def hookies():
    for hookie_path in HOOKIES_PATHS:
        if path.isdir(hookie_path):
            print('Such hookie dir already exists')

        if not path.isdir(hookie_path):
            os.makedirs(hookie_path)
            print('Created')


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    initfs()
    initdb()
    hookies()
