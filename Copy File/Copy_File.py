import shutil
import os

try : 
    filename1 = str(input("Enter File Name 1 'Src' : "))
    filename2 = str(input("Enter File Name 2  'Dest': "))
    if os.path.exists(filename1) and os.path.isfile(filename1):
        shutil.copyfile(filename1, filename2)
    print("File Copy ...!")
except FileNotFoundError:
    print("File Not Found !")


