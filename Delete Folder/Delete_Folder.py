import os
import shutil

try:
    dirname = str(input("Enter Directory Name : "))
    if os.path.exists(dirname) and os.path.isdir(dirname):
        print("R For Empty Foldr .")
        print("RF for Contain Folder .")
        dir_mod = str(input("Enter ('R'/'RF') "))
        if dir_mod.upper() == 'R':
            os.rmdir(dirname)
            print("Directory Have Ben Deleted !")
        elif dir_mod.upper() == 'RF':
            shutil.rmtree(dirname)
            print("Directory Have Ben Deleted !")
except OSError:
    print("Directory Not Empty !")
except FileNotFoundError:
    print("Directory Not Found !")
