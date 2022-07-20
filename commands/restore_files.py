import os
import shutil
from os import path
from zipfile import ZipFile

BASE_DIR = '.zeon_git'


def confirm_restore():
    confirm = input("Are you sure you want to run restore? (y/n): ").lower()

    if confirm == "y":
        if not path.exists('backup.zip'):
            print('Does not exist such zipfile')
            exit()

    elif confirm == "n":
        exit()
    else:
        print("Use only 'y' or 'n'")
        exit()


def del_git():
    for item in os.listdir(BASE_DIR):
        file_path = os.path.join(BASE_DIR, item)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print('The content of .zeon_git was deleted')
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def restorefiles():
    confirm_restore()
    del_git()

    file_name = "backup.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        zip.extractall('.')
        print('Restoration done!')
