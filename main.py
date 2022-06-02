import os
import sys
from os import path

args = sys.argv
print(args)

if len(args) != 2:
    print('Should be 1 argument')
    exit(0)

commands = ['init', 'add', 'del', 'list']

if commands[0] == args[1]:
    print(f'Была вызвана команда : {args[1]}')

if commands[1] == args[1]:
    print(f'Была вызвана команда : {args[1]}')

if commands[2] == args[1]:
    print(f'Была вызвана команда : {args[1]}')

if commands[3] == args[1]:
    print(f'Была вызвана команда : {args[1]}')



