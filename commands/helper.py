import os
import multiprocessing
import subprocess
import sys
from pathlib import Path


args = sys.argv


def run_hook(status, command):
    hooks = sorted(os.listdir(f'hookies/{command}/{status}/'))
    with_at = []
    list_hooks = []
    for hook in hooks:
        hook_name = Path(hook).stem
        if '@' in hook_name:
            with_at.append(hook)
        else:
            list_hooks.append(hook)

    if with_at != []:
        list_hooks.insert(2, with_at)

    for hook in list_hooks:
        if isinstance(hook,list):
            if Path(f'hookies/{command}/{status}/{hook[0]}').is_file() and Path(f'hookies/{command}/{status}/{hook[1]}').is_file():
                subprocess.call(f'python3 hookies/{command}/{status}/{hook[0]}', shell=True)
                subprocess.call(f'python3 hookies/{command}/{status}/{hook[1]}', shell=True)

        if Path(f'hookies/{command}/{status}/{hook}').is_file():
            subprocess.call(f'python3 hookies/{command}/{status}/{hook}', shell=True)

    # for hook in list_hooks:
    #     if Path(f'hookies/{command}/{status}/{hook}').is_file():
            # print(f'python3 hookies/{command}/{status}/{hook}')
            # subprocess.Popen(f'python3 hookies/{command}/{status}/{hook}', shell=True, stdout=subprocess.PIPE)
            # p = multiprocessing.Process(target=run_hook(hook))
            # print(p)
            # subprocess.call(f'python3 hookies/{command}/{status}/{hook}', shell=True)

def init_list(args):
    pass
    # if len(args) != 1:
    #     print('Should be just 1 argument')
    #     exit(0)


def del_file(args):
    pass
    # if len(args) != 2:
    #     print('Should be just 2 arguments')
    #     exit()


def add_file(args):
    pass
    # if len(args) < 2:
    #     print('Should be just 3 arguments')
    #     exit()

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



