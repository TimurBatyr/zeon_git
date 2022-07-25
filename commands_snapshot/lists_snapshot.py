import os

SNAPSHOT_DIR = 'snapshots'


def lists_ssht():
    files_list = os.listdir(SNAPSHOT_DIR)
    print(f'Number of files: {len(files_list)}\n')
    for files in files_list:
        print(f'---{files}')