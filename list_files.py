import os
import sys
from os import path

args = sys.argv
print(args)

BASE_DIR = 'zeon_fs2'

if len(args) != 1:
    print('Should be no argument')
    exit(0)


files_list = os.listdir(BASE_DIR)
print(f'Files:{len(files_list)}\n')
for i in files_list:
    print(i)
    exit(0)


