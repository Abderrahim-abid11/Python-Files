import os

try:
    filename = str(input("Enter Name of File : "))
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Exist .")
