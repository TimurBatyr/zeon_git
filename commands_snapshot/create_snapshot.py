import fcntl
import os

from os import path
from zipfile import ZipFile

BASE_DIR = '.zeon_git'
SNAPSHOT_DIR = 'snapshots'


def create_ssht(args):
    if not path.isdir(SNAPSHOT_DIR):
        os.mkdir(SNAPSHOT_DIR)
        print('Created snapshot dir')

    if path.isfile(SNAPSHOT_DIR + f'/{args[2]}'):
        print('Already file exists in snapshots')
    else:
        zipfile = ZipFile(f'{SNAPSHOT_DIR}/{args[2]}', 'w')
        for root, dirs, files in os.walk(BASE_DIR):
            for f in files:
                with open(os.path.join(root, f), 'a') as file:
                    fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    zipfile.write(os.path.join(root, f))
                    fcntl.flock(file, fcntl.LOCK_UN)
        print(f'Created snapshot: {args[2]}')
        zipfile.close()
        zipfile.printdir()
