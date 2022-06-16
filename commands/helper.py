import os
import sys
from pathlib import Path

args = sys.argv
# print(args)
# print(len(args))


def init_list(args):
    if len(args) != 1:
        print('Should be just 1 argument')
        exit(0)


def del_file(args):
    if len(args) != 2:
        print('Should be just 2 arguments')
        exit()


def add_file(args):
    if len(args) < 2:
        print('Should be just 3 arguments')
        exit()



def find_dir():
    abs_path = os.getcwd()
    directory = '.zeon_git'

    if os.path.exists((abs_path) + f'/{directory}'):
        print(f'Dir found here -> {abs_path}')
    else:
        while True:
            abs_path = Path(abs_path).parent
            # if os.path.exists(str(abs_path) + '/{directory}'):
            if directory in os.listdir(abs_path):
                print(f'Dir found here -> {abs_path}')
                break
            if str(abs_path) == '/':
                break



