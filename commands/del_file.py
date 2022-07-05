import os
import sys

from commands.add_file import hash_content

args = sys.argv
# print(args)

BASE_DIR = '.zeon_git'
OBJECTS_PATH = f'{BASE_DIR}/objects'
DATABASE_PATH = f'{BASE_DIR}/index.txt'


def delfile(args):
    full_path = (OBJECTS_PATH + f'/{args[1]}')
    data = []

    with open(DATABASE_PATH, 'r') as index:
        hashes = index.read()
        if len(args) <= 2:
            for line in hashes.split('\n'):
                if not full_path.lstrip('/') in line:
                    data.append(line)
        else:
            for line in hashes.split('\n'):
                if not (OBJECTS_PATH + f'/{args[2].lstrip("/")}') in line:
                    data.append(line)

    with open(DATABASE_PATH, 'w') as file:
        file.write('\n'.join(data))

    with open(DATABASE_PATH, 'r') as index:
        hashes = index.read()
        try:
            if not hash_content(args) in hashes:
                os.remove(OBJECTS_PATH + f'/{hash_content(args)}')
                print('Deleted from objects')
                exit()
        except FileNotFoundError:
            print('Already deleted hash-file')


if __name__ == '__main__':
    from helper import del_file
    args = sys.argv
    del_file(args)
    delfile(args)
