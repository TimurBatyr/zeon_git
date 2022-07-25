import os
from os import path
from hashlib import md5

SNAPSHOT_DIR = 'snapshots'
TEMP_DIR = 'temp_dir/.zeon_git/objects'


def hash_content():
    pass
    # for root, dirs, files in os.walk(TEMP_DIR):
    #     for f in files:
    #         os.rename(f, f + '.txt')
    #         print(f)

            # with open(f, 'r') as file:
                # hashed_content = md5(file.read().encode()).hexdigest()
                # return hashed_content



def commit_ssht(args):
    hash_content()
    print('commmmit')