from os import walk, sep
from os.path import basename, isdir
from sys import argv

def tree(startpath):
    for root, subdirs, files in walk(startpath):
        level = root.replace(startpath, '').count(sep)
        indent = '  | ' * (level-1) + '  ├── '
        print ("%s%s/" % (indent, basename(root)))
        subindent = '  | ' * (level) + '  └──  '
        for f in files:
            print ("%s%s" % (subindent, f))
            
if __name__ == '__main__':
    if len(sys.argv) == 0:
        print('.')
        tree(os.getcwd)
    else:
        tree(os.getcwd)
