import sys
import os
import re
import subprocess

c_dir = 0
c_file = 0

def print_tree(path, indent=""):

    files = os.listdir(path)
    
    global c_dir
    global c_file
    
    for i in range(0, len(files)):
        fullpath = path + "/" + files[i]

        if os.path.isfile(fullpath):
            c_file += 1 
        if i == len(files) - 1:
            print(indent + "└── " + files[i])
        else:
            print(indent + "├── " + files[i])


        if os.path.isdir(fullpath):
            c_dir += 1 
            if i == len(files) - 1:
                print_tree(fullpath, indent+ "    ")
            else:
                print_tree(fullpath, indent+ "│   ")



if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
    print_tree(cwd)
else:
    cwd = sys.argv[1]
    print(cwd)
    print_tree(cwd)
    
print("\n" + str(c_dir) + " directories, " + str(c_file) + " files")
