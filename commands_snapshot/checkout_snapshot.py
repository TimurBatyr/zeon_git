import os
from os import path
from zipfile import ZipFile

SNAPSHOT_DIR = 'snapshots'
TEMP_DIR = 'temp_dir'


def checkout_ssht(args):
    if not path.isdir(TEMP_DIR):
        os.mkdir(TEMP_DIR)
        print('Temporary dir created')
    else:
        print('Such temporary dir exists')

    file_name = SNAPSHOT_DIR + f'/{args[2]}'
    if not path.isfile(file_name):
        print('Do not exist such zip file')
        exit(0)

    with ZipFile(file_name, 'r') as zip:
        zip.extractall(TEMP_DIR)
        print('Restoration done to temporary dir!')
