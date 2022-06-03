import os
import sys
from pathlib import Path

args = sys.argv
print(args)

if len(args) != 3:
    print('Should not be more than 3 argument')

if len(args) == 1:
    print('Add arguments')
    exit(0)

commands = {
    'init': 'init_fs.py',
    'add': 'add_file.py',
    'del': 'del_file.py',
    'list': 'list_files.py',
    'get': 'get_file',
}


if args[1] in commands:
    print(f'Command called is : {args[1]}')

elif not args[1] in commands:
    print(f'Such command does not exist')
    exit(0)


#Step-7
if args[1] == list(commands)[0]:
    os.system(f'python3 {commands.get(args[1])}')

elif args[1] == list(commands)[1]:
    os.system(f'python3 {commands.get(args[1])} {args[2]}')

elif args[1] == list(commands)[2]:
    os.system(f'python3 {commands.get(args[1])} {args[2]}')

elif args[1] == list(commands)[3]:
    os.system(f'python3 {commands.get(args[1])}')





