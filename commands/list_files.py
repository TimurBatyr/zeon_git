import sys


def listfiles():
    BASE_DIR = '.zeon_git'
    DATABASE_PATH = f'{BASE_DIR}/index.txt'
    elements = []
    files = {}

    with open(DATABASE_PATH, 'r') as file:
        for item in (file.read()).split('\n'):
            elements.append(item.split(',')[0])

    for element in elements:
        link = files
        for path in element.split('/'):
            if not path in link:
                link[path] = {}
            link = link[path]
    print(files)

    def to_tree(d, c=0):
        for a, b in d.items():
            # value_if_true condition else value_if_else
            yield '   '.join('|' for _ in range(c + 1)) + (f'---{a}' if d[a] == {} else f'---{a}/')
            yield from ([] if b is None else to_tree(b, c + 1))

    print('\n'.join(to_tree(files)))


if __name__ == '__main__':
    from helper import init_list
    args = sys.argv
    init_list(args)
    listfiles()






