import fcntl
import os
import sys
from os import path
from zipfile import ZipFile

BASE_DIR = '.zeon_git'
SNAPSHOT_DIR = 'snapshots'

def create_ssht(args):
    if path.isfile(SNAPSHOT_DIR + f'/{args[1]}'):
        print('Already file exists in snapshots')
    else:
        zipfile = ZipFile(f'{SNAPSHOT_DIR}/{args[1]}', 'w')
        for root, dirs, files in os.walk(BASE_DIR):
            for f in files:
                with open(os.path.join(root, f), 'a') as file:
                    fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    zipfile.write(os.path.join(root, f))
                    fcntl.flock(file, fcntl.LOCK_UN)
        print('Created snapshot')
        zipfile.close()
