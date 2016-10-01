#!/usr/bin/env python3

import subprocess
from os import walk, sep
from os.path import basename, isdir
import sys

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
    if (len(sys.argv) == 1):
        path = '.'
    elif (len(sys.argv) == 2):
        path = sys.argv[1]
    else:
        print('Invalid arguments.')
    tree(path)
    print()
