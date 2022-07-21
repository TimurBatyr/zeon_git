import fcntl
import time

import flock
import os
from os import path
from zipfile import ZipFile

BASE_DIR = '.zeon_git'


def confirm_backup():
    confirm = input('Are you sure you want to run backup? (y/n): ').lower()

    if confirm == 'y':
        if not path.exists(BASE_DIR):
            print('Does not exist such dir')

    elif confirm == 'n':
        exit()
    else:
        print("Use only 'y' or 'n'")
        exit()


def backupfiles():
    confirm_backup()

    zipfile = ZipFile('backup.zip', 'w')
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            with open(os.path.join(root, f), 'a') as file:
                fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                zipfile.write(os.path.join(root, f))
                # os.access(os.path.join(root, file))
                # time.sleep(10)
                fcntl.flock(file, fcntl.LOCK_UN)
    zipfile.close()


