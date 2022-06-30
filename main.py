import os
import sys


from commands import del_file, add_file, init_fs, list_files, helper

args = sys.argv
print(args)

if len(args) > 4:
    print('Should not be more than 3 argument')
    exit()

elif len(args) == 1:
    helper.find_dir()
    exit()


elif (args[1] == 'add' or args[1] == 'del') and len(args) == 2:
    print('Add one more argument')
    exit()

elif (args[1] == 'list' or args[1] == 'init') and len(args) > 2:
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


if __name__ == '__main__':
    if args[1] == list(commands)[0]: # init
        print(os.path.abspath(os.path.curdir))
        init_fs.initfs()
        init_fs.initdb()

    elif args[1] == list(commands)[1]: # add
        add_file.addfile(args[1:4])

    elif args[1] == list(commands)[2]: # del
        del_file.delfile(args[1:4])

    elif args[1] == list(commands)[3]: # list
        list_files.listfiles()



