import sys
import time

from commands import del_file, add_file, init_fs, list_files, helper, backup_files, restore_files
from commands_snapshot import create_snapshot, lists_snapshot, dels_snapshot, restores_snapshot, checkout_snapshot, \
    commit_snapshot

args = sys.argv
# print(args)

if len(args) > 5:
    print('Should not be more than 4 argument')
    exit()

elif len(args) == 1:
    helper.find_dir()
    exit()

elif (args[1] == 'add' or args[1] == 'del') and len(args) == 2:
    print('Add one more argument')
    exit()

elif (args[1] == 'list' or args[1] == 'init' or args[1] == 'backup') and len(args) > 2:
    print('Excess of args')
    exit()

elif args[1] == 'snapshot' and len(args) == 2:
    print('Add or delete some args')
    exit()


commands = {
    'init': 'init_fs.py',
    'add': 'add_file.py',
    'del': 'del_file.py',
    'list': 'list_files.py',
    'backup': 'backup_files.py',
    'restore': 'restore_files.py',
}

commands_snapshot = {
    'create': 'create_snapshot.py',
    'list': 'lists_snapshot.py',
    'del': 'dels_snapshot.py',
    'restore': 'restores_snapshot.py',
    'checkout': 'checkout_snapshot.py',
    'commit': 'commit_snapshot.py',

}


if args[1] in commands:
    print(f'Command called is : {args[1]}')

elif args[2] in commands_snapshot:
    print(f'Command called is : {args[1]} {args[2]}')

elif not args[1] in commands:
    print(f'Such command does not exist')
    exit(0)


if __name__ == '__main__':
    if args[1] == list(commands)[0]: # init
        # print(os.path.abspath(os.path.curdir))
        helper.run_hook('pre_hook', 'init')
        init_fs.initfs()
        init_fs.initdb()
        # time.sleep(10)
        helper.run_hook('post_hook', 'init')

    elif args[1] == list(commands)[1]: # add
        add_file.addfile(args[1:4])

    elif args[1] == list(commands)[2]: # del
        del_file.delfile(args[1:4])

    elif args[1] == list(commands)[3]: # list
        list_files.listfiles()

    elif args[1] == list(commands)[4]: # backup
        backup_files.backupfiles()

    elif args[1] == list(commands)[5]: # restore
        restore_files.restorefiles()

    #snapshots
    elif args[2] == list(commands_snapshot)[0]: #snapshot create
        create_snapshot.create_ssht(args[1:4])

    elif args[2] == list(commands_snapshot)[1]: #snapshot list
        lists_snapshot.lists_ssht()

    elif args[2] == list(commands_snapshot)[2]: #snapshot del
        dels_snapshot.dels_ssht(args[1:4])

    elif args[2] == list(commands_snapshot)[3]: #snapshot restore
        restores_snapshot.restores_ssht(args[1:4])

    elif args[2] == list(commands_snapshot)[4]: #snapshot checkout
        checkout_snapshot.checkout_ssht(args[1:4])

    elif args[2] == list(commands_snapshot)[5]: #snapshot commit
        commit_snapshot.commit_ssht(args[1:5])
