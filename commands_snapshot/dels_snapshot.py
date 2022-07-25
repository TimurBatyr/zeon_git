import os

from os import path

SNAPSHOT_DIR = 'snapshots'


def dels_ssht(args):
    file_name = SNAPSHOT_DIR + f'/{args[2]}'

    if not path.isfile(file_name):
       print('Do not exist such file')
       exit(0)

    if path.isfile(file_name):
        os.remove(file_name)
        print('Zipfile deleted')
        exit(0)
