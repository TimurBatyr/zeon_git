import os
from os import path
from zipfile import ZipFile

SNAPSHOT_DIR = 'snapshots'
TEMP_DIR = 'temp_dir'


def checkout_ssht(args):
    # zip_file = SNAPSHOT_DIR + f'/{args[2]}'
    # target_file = '.zeon_git/objects/' + f'{(args[3]).lstrip("/")}'
    # print(target_file)
    #
    # with ZipFile(zip_file, 'r') as zip_obj:
    #     # zip_obj.printdir()
    #     with open('.zeon_git/index.txt', 'r') as db:
    #         index_db = list(filter(len, map(str.strip, db.readlines())))
    #         for path_db in index_db:
    #             if target_file in path_db:
    #                 file_name = (path_db.split(','))[1]
    #                 print(file_name)
    #                 # print(f'.zeon_git/objects/{file_name}')
    #                 zip_obj.extract(f'.zeon_git/objects/{file_name}', TEMP_DIR)


    file_name = SNAPSHOT_DIR + f'/{args[2]}'

    if not path.isfile(file_name):
        exit('Do not exist such zip file')

    if not path.isdir(TEMP_DIR):
        os.mkdir(TEMP_DIR)
        print('Temporary dir created')
    else:
        print('Such temporary dir exists')

    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        zip.extractall(TEMP_DIR)
        print('Restoration done to temporary dir!')

    with open(f'{TEMP_DIR}/zip_name.txt', 'w') as file:
        file.write(args[2])
