#!/usr/bin/env python3

import sys
import os
import re

def print_tree(path, indent=""):
    
    files = os.listdir(path)
    for i in range(0, len(files)):
        fullpath = path + "/" + files[i]
        
        if i == len(files) - 1:
            print indent + '└──' + files[i]
        else:
            print indent + '├── ' + files[i]
            
            
        if os.path.isdir(fullpath):
            if i == len(files) - 1:
                print_tree(fullpath, indent+ '    ')
            else:
                print_tree(fullpath, indent+ '|    ')

                
if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
    print_tree(cwd)
else:
    cwd = sys.argv[1]
    print(cwd)
    print_tree(cwd)
