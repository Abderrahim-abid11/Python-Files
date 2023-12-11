import os 

try:
    filename = str(input("Enter File Name : "))
    if os.path.exists(filename):
        os.remove(filename)
        print("File have ben deletet !")
except PermissionError: 
    print("Do Not Have Permission .")
except FileNotFoundError:
    print("File Not Exist !")
