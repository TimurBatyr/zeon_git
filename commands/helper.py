import os
import sys

args = sys.argv
# print(args)
# print(len(args))


def init_list(args):
    if len(args) != 1:
        print('Should be just 1 argument')
        exit(0)


def add_del(args):
    if len(args) != 2:
        print('Should be just 2 arguments')
        exit()


# def get_dir(args):
#     path = os.getcwd().split('/')
#
#     directory = '.zeon_fs'
#     index = 0
#
#     while index > len(path):
#         if directory in os.listdir('/'.join(path[:-1])):
#             print(f'Directory named "{directory}" is here: {"/".join(path[:-1])}')
#             break
#         index += 1
#     print("Not")






