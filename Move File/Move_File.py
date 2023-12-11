import os

filename = str(input("Enter File Name : "))
dirname = str(input("Enter Directory Name (dir/file-name): "))

try:
    if os.path.exists(dirname):
        print("Is Already There !")
    else :
        os.replace(filename, dirname)
        print(f"{filename} Have Ben Moved !")
except FileNotFoundError:
    print("File Not Found !")
