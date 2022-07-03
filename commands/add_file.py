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

    if not path.isfile(args[1]):
        print('It is not a file or does not exist such file')
        exit(0)

    hashed_name = hash_content(args)

    if path.isfile(OBJECTS_PATH + f'/{hashed_name}'):
        print('Already file exists in objects')

    else:
        shutil.copyfile(args[1], OBJECTS_PATH + f'/{hashed_name}')
        print('Added a file to objects')

    add_to_db(args)


def add_to_db(args):
    file_name = Path(args[1]).name

    with open(DATABASE_PATH, 'r') as index:
        hashes = index.read()
        if len(args) <=2:
            if not ((OBJECTS_PATH + f'/{args[1]}') in hashes):
                with open(DATABASE_PATH, 'a') as file:
                    file.write(OBJECTS_PATH + f'/{file_name},{hash_content(args)}\n')
                    print('Added hash to index')
                    exit()
            print('Such path exists in db')
            exit()

        make_dir = args[2]
        path_to = (os.path.join(OBJECTS_PATH, make_dir.lstrip('/')))

        if not path_to in hashes and args[2].endswith('/') or args[2].endswith('.*'):
            with open(DATABASE_PATH, 'a') as file:
                file.write(f'{path_to}{file_name},{hash_content(args)}\n')
                print('Added hash to index')
                exit()


        if not path_to in hashes:
            with open(DATABASE_PATH, 'a') as file:
                file.write(f'{path_to},{hash_content(args)}\n')
                print('Added hash to index')
                exit()

        # if path_to in hashes:
        print('Such path exists in db')
        exit()


if __name__ == '__main__':
    from helper import add_file
    args = sys.argv
    add_file(args)
    addfile(args)

