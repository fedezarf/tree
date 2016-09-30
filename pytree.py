from os import walk, sep
from os.path import basename, isdir
from sys import argv

def tree(startpath):
    for root, subdirs, files in walk(startpath):
        level = root.replace(startpath, '').count(sep)
        indent = '  | ' * (level - 1) + '  ├── '
        print("%s%s/" % (indent, basename(root)))
        subindent_1 = '  | ' * (level) + '  ├──  '
        subindent_2 = '  | ' * (level) + '  └──  '
        for i, j in enumerate(files):
            if (i == len(files) - 1):
                print("%s%s" % (subindent_2, j))
            else:
                print("%s%s" % (subindent_1, j))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        tree(os.getcwd)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        tree(sys.argv[1])
