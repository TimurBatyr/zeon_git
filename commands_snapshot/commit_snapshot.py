import fcntl
import os
import pathlib
import shutil

from hashlib import md5
from zipfile import ZipFile


BASE_DIR = '.zeon_git'
SNAPSHOT_DIR = 'snapshots'
TEMP_DIR = 'temp_dir/.zeon_git/index.txt'
TEMP_SUBDIR = 'temp_dir/.zeon_git/objects'


def hash_content(args):
    with open(args, 'r') as file:
        hashed_content = md5(file.read().encode()).hexdigest()
        #print(hashed_content)
        return hashed_content


def commit_ssht(args):
    hashed_file = hash_content(args[3])

    with open(TEMP_DIR, 'r') as db:
        index_db = list(filter(len, map(str.strip, db.readlines())))
        # print(index_db)
        for path_db in index_db:
            if args[2] in path_db:
                file_name = (path_db.split(','))[1]
                change_path = args[2].rsplit('/', 1)[0]
                list_path = list(map(lambda item: item.replace(f'{",".join((args[2],file_name))}',
                                                               f'{change_path}/{args[3]},{hashed_file}'), index_db))
                with open(TEMP_DIR, 'w') as f:
                    for item in list_path:
                        with open(TEMP_DIR, 'a') as file:
                            file.write(f'{item}\n')
                    print('Replaced path/hash in index')

                check_db = ' '.join(map(str, list_path))
                if not file_name in check_db:
                    os.unlink(f'{TEMP_SUBDIR}/{file_name}')
                    print('Deleted hash name')

    if hashed_file in (os.listdir(TEMP_SUBDIR)):
        print('Such file exist')
    else:
        shutil.copyfile(args[3], TEMP_SUBDIR + f'/{hashed_file}')
        print('Added a file to objects')


    '''Замена zip файла'''
    with open('temp_dir/zip_name.txt', 'r') as file:
        zip_name = file.readline()

    directory = pathlib.Path("temp_dir/")
    zipfile = ZipFile(f'temp_dir/{zip_name}', 'w')
    src = os.path.abspath(f'{directory}/{BASE_DIR}')
    for root, dirs, files in os.walk(f'{directory}/{BASE_DIR}'):
        for f in files:
            src_name = os.path.abspath(os.path.join(root, f))
            arcname = f'{BASE_DIR}/{src_name[len(src) + 1:]}'
            print(arcname)
            with open(os.path.join(root, f), 'a') as file:
                fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                zipfile.write(src_name, arcname)
                fcntl.flock(file, fcntl.LOCK_UN)
    print('Created snapshot')
    zipfile.close()
    zipfile.printdir()

    os.system(f'mv temp_dir/{zip_name} snapshots/')

    shutil.rmtree('temp_dir')

