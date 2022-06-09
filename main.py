import os
import sys
from os import path

from commands import del_file, add_file, init_fs, list_files, helper

args = sys.argv
print(args)

if len(args) > 3:
    print('Should not be more than 3 argument')
    exit()

elif len(args) == 1:
    # helper.get_dir(args)
    print('Add two more arguments')
    exit()

elif (args[1] == 'add' or args[1] == 'del') and len(args) == 2:
    print('Add one more argument')
    exit()

elif (args[1] == 'list' or args[1] == 'list') and len(args) > 2:
    print('Excess of args')
    exit()


commands = {
    'init': 'init_fs.py',
    'add': 'add_file.py',
    'del': 'del_file.py',
    'list': 'list_files.py',
}


if args[1] in commands:
    print(f'Command called is : {args[1]}')

elif not args[1] in commands:
    print(f'Such command does not exist')
    exit(0)


#Step-7
# if args[1] == list(commands)[0]:
#     os.system(f'python3 {commands.get(args[1])}')
#
# elif args[1] == list(commands)[1]:
#     os.system(f'python3 {commands.get(args[1])} {args[2]}')
#
# elif args[1] == list(commands)[2]:
#     os.system(f'python3 {commands.get(args[1])} {args[2]}')

# elif args[1] == list(commands)[3]:
#     os.system(f'python3 {commands.get(args[1])}')


#Step-8, 10

if __name__ == '__main__':
    if args[1] == list(commands)[0]: # init
        print(os.path.abspath(__file__))
        init_fs.initfs()

    elif args[1] == list(commands)[1]: # add
        add_file.addfile(args[1:3])

    elif args[1] == list(commands)[2]: # del
        del_file.delfile(args[1:3])

    elif args[1] == list(commands)[3]: # list
        list_files.listfiles()


