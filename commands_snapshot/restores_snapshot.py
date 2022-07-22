import os
import shutil
from os import path
from zipfile import ZipFile


BASE_DIR = '.zeon_git'
INTERIM_DIR = '.zeon_git_interim'
SNAPSHOT_DIR = 'snapshots'


def del_zeon_git(dir):
    for item in os.listdir(dir):
        file_path = os.path.join(dir, item)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f'The content of {dir} was restored')
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def restores_ssht(args):
    if not path.isdir(BASE_DIR):
        print('Such dir does not exist')

    file_name = SNAPSHOT_DIR + f'/{args[2]}'
    if not path.isfile(file_name):
        print('Do not exist such zip file')
        exit(0)

    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        zip.extractall(INTERIM_DIR)
        print('Restoration done!')

    if path.isdir(BASE_DIR):
        del_zeon_git(BASE_DIR)

    os.system(f'mv {INTERIM_DIR}/.zeon_git ./')

    if path.isdir(BASE_DIR):
        os.rmdir(INTERIM_DIR)
