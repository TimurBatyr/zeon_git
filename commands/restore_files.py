import os
import shutil
from os import path
from zipfile import ZipFile

BASE_DIR = '.zeon_git'
INTERIM_DIR = '.zeon_git_interim'


def confirm_restore():
    confirm = input('Are you sure you want to run restore? (y/n): ').lower()

    if confirm == 'y':
        if not path.exists('backup.zip'):
            print('Does not exist such zipfile')
            exit()

    elif confirm == 'n':
        exit()
    else:
        print("Use only 'y' or 'n'")
        exit()


def del_zeon_git(dir):
    for item in os.listdir(dir):
        file_path = os.path.join(dir, item)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f'The content of {dir} was deleted')
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def restorefiles():
    confirm_restore()

    if not path.isdir(BASE_DIR):
        print('Such dir does not exist')
        exit()

    file_name = "backup.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        zip.extractall(INTERIM_DIR)
        print('Restoration done!')

    if path.isdir(BASE_DIR):
        del_zeon_git(BASE_DIR)

    os.system(f'mv {INTERIM_DIR}/.zeon_git ./')

    if path.isdir(BASE_DIR):
        os.rmdir(INTERIM_DIR)
