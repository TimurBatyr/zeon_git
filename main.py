import sys

args = sys.argv
print(args)

if len(args) != 2:
    print('Should be 1 argument')
    exit(0)

commands = ('init', 'add', 'del', 'list')

if args[1] in commands:
    print(f'Command called is : {args[1]}')
    exit(0)
else:
    print(f'Such command does not exist')
    exit(0)






