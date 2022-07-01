import os
import shutil
import sys
from hashlib import md5
from os import path
from pathlib import Path

BASE_DIR = '.zeon_git'
OBJECTS_PATH = f'{BASE_DIR}/objects'
DATABASE_PATH = f'{BASE_DIR}/index.txt'


def hash_content(args):
    with open(args[1], 'r') as file:
        hashed_content = md5(file.read().encode()).hexdigest()
        return hashed_content


def addfile(args):
    hashed_name = hash_content(args)

    if len(args) <= 2:
        if not path.isfile(args[1]):
            print('It is not a file')
            exit(0)
        elif path.isfile(OBJECTS_PATH + f'/{hashed_name}'):
            print('Already exists file')
            # exit(0)
        shutil.copyfile(args[1], OBJECTS_PATH + f'/{hashed_name}')
        print('Added a file')

    add_to_db(args)


def add_to_db(args):
    # file_name = Path(args[1]).name

    with open(DATABASE_PATH, 'r') as index:
        hashes = index.read()
        if len(args) <=2:
            if not ((OBJECTS_PATH + f'/{args[1]}') in hashes):
                with open(DATABASE_PATH, 'a') as file:
                    file.seek(0, 0)
                    file.write(OBJECTS_PATH + f'/{args[1]},{hash_content(args)}\n')
                    print('Added hash to index')
                    exit()
            print('Such path exists')
            exit()
        elif len(args) <= 3:
            if not ((OBJECTS_PATH + f'/{args[2].lstrip("/")}') in hashes):
                with open(DATABASE_PATH, 'a') as file:
                    file.seek(0, 0)
                    file.write(OBJECTS_PATH + f'/{args[2].lstrip("/")},{hash_content(args)}\n')
                    print('Added hash to index')
                    exit()
            elif (OBJECTS_PATH + f'/{args[2].lstrip("/")}') in hashes:
                print('Such path exists')
                exit()
            else:
                with open(DATABASE_PATH, 'a') as file:
                    file.seek(0, 0)
                    file.write(OBJECTS_PATH + f'/{args[1]},{hash_content(args)}\n')
                    print('Added hash to index')
                    exit()




if __name__ == '__main__':
    from helper import add_file
    args = sys.argv
    add_file(args)
    addfile(args)

