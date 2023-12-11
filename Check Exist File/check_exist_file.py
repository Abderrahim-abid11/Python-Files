import os

filename = str(input("Enter File Name : "))
if os.path.exists(filename) and os.path.isfile(filename):
    print("File Exist !")
else:
    print("File Not Exist !")
