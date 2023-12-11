import os

filename = str(input("Enter your Folder Name : "))

if os.path.exists(filename) and os.path.isdir(filename):
    print("Folder Exist !")
else:
    print("Folder Not Exist !")
