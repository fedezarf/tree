#!/usr/bin/env python3
import sys
import os
import re
import subprocess

c_dir = 0
c_file = 0


def new_sort(input):
    return re.sub('[^a-zA-Z0-9]', '', input).lower()


def lsort(path):
    c = [x for x in os.listdir(path) if not x.startswith('.')]
    return sorted(c, key=new_sort)


def print_tree(path, indent=""):

    files = lsort(path)

    global c_dir
    global c_file

    for i in range(0, len(files)):
        fullpath = path + "/" + files[i]

        g_update(fullpath)

        if i == len(files) - 1:
            print(indent + "└── " + files[i])
        else:
            print(indent + "├── " + files[i])

        if os.path.isdir(fullpath):
            c_dir += 1
            if i == len(files) - 1:
                print_tree(fullpath, indent + "    ")
            else:
                print_tree(fullpath, indent + "│   ")


def g_update(f):
    global c_file
    if os.path.isfile(f):
        c_file += 1

if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
    print_tree(cwd)
else:
    cwd = sys.argv[1]
    print(cwd)
    print_tree(cwd)

print()
print(str(c_dir) + (" directories, " if c_dir != 1 else " directorie, ") + str(c_file) + (" files" if c_file != 1 else " files"))
