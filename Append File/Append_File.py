import os

try:
    filename = str(input("Enter File Name : "))
    text = str(input("Enter Your Text : "))
    with open(filename, "a") as file:
        file.write(text)
        file.write("\n")
except FileNotFoundError:
    print("File Not Found !")
